"""
Banking System — Level 3

New spec:
  - schedule_payment(from_id, to_id, amount, execute_at) — schedule a
    transfer to execute at a future time. Returns a payment_id.
  - cancel_payment(payment_id) — cancel a not-yet-executed payment.

What changed from L2:
  - ScheduledPayment dataclass, ordered by execute_at for heap usage
  - _scheduled: min-heap of pending payments
  - _pending_by_id: lookup for cancellation
  - _current_time: monotonic, tracks "system time"
  - _advance_time(): the key new helper — called by every public method
    that takes a timestamp. Drains all due scheduled payments before
    serving the new request. This avoids needing a background thread.
  - _do_transfer(): factored out of transfer() so the scheduled-payment
    processor can call it too.

The L1 over-build (timestamp parameter on every method) pays off here.
Without it we couldn't have a notion of "system time has advanced to T,
process anything due at or before T." Adding timestamps now would
require changing every method signature.

Key design decisions:

  1. LAZY PROCESSING. Scheduled payments execute when the next operation
     advances time past their execute_at. No background thread, no
     concurrency, fully deterministic. Trade-off: if no operation runs
     for a long time, scheduled payments stay pending. That's the right
     behaviour here because there are no side effects (no emails sent
     etc.) — execution is only observable through subsequent operations.

  2. TOMBSTONE CANCELLATION. We don't remove cancelled payments from
     the heap (that's O(n) for arbitrary removal). We set a flag and
     skip them at drain time. Cancellation is O(1); drain wastes a
     tiny amount of work on cancelled entries.

  3. MONOTONIC TIME. _advance_time refuses to go backwards. Real banking
     systems care about this for audit trails — events have an immutable
     order. If you accept out-of-order timestamps you lose that guarantee.

  4. BEST-EFFORT EXECUTION. A scheduled payment that can't execute
     (insufficient funds at execution time) is silently dropped. Real
     systems would retry / DLQ; we don't have spec for that, so we
     pick the simplest defensible behaviour.

Still NOT building:
  - Aliases / merge — L4 territory
"""

from dataclasses import dataclass, field
from enum import Enum
from heapq import heappush, heappop
from typing import Optional
from uuid import uuid4


class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TRANSFER_OUT = "transfer_out"
    TRANSFER_IN = "transfer_in"


@dataclass(frozen=True)
class Transaction:
    txn_id: str
    timestamp: int
    type: TransactionType
    amount: int
    counterparty: Optional[str] = None


@dataclass
class Account:
    account_id: str
    balance: int = 0
    log: list[Transaction] = field(default_factory=list)

    _CREDIT_TYPES = frozenset({
        TransactionType.DEPOSIT,
        TransactionType.TRANSFER_IN,
    })

    def apply(self, txn: Transaction) -> None:
        if txn.type in self._CREDIT_TYPES:
            self.balance += txn.amount
        else:
            self.balance -= txn.amount
        self.log.append(txn)

    def total_volume(self) -> int:
        return sum(t.amount for t in self.log)

    def transaction_count(self) -> int:
        return len(self.log)


@dataclass(order=True)
class ScheduledPayment:
    """Ordered by execute_at so we can use it directly in a heap.

    dataclass(order=True) generates __lt__ across all fields in
    declaration order. We mark all fields except execute_at as
    compare=False so only execute_at participates in ordering.
    """
    execute_at: int
    payment_id: str = field(compare=False)
    from_id: str = field(compare=False)
    to_id: str = field(compare=False)
    amount: int = field(compare=False)
    cancelled: bool = field(default=False, compare=False)


class AccountNotFoundError(Exception): pass
class DuplicateAccountError(Exception): pass
class InsufficientFundsError(Exception): pass
class TimeWentBackwardsError(Exception): pass


class BankingSystem:
    def __init__(self):
        self._accounts: dict[str, Account] = {}
        self._scheduled: list[ScheduledPayment] = []
        self._pending_by_id: dict[str, ScheduledPayment] = {}
        self._current_time: int = 0

    # --- internal helpers --------------------------------------------------

    def _get(self, account_id: str) -> Account:
        if account_id not in self._accounts:
            raise AccountNotFoundError(account_id)
        return self._accounts[account_id]

    def _advance_time(self, timestamp: int) -> None:
        """Advance system time, processing due scheduled payments.

        Called by every public method that takes a timestamp. This is
        what makes scheduled payments work without a background thread.
        """
        if timestamp < self._current_time:
            raise TimeWentBackwardsError(
                f"Operation timestamp {timestamp} < current {self._current_time}"
            )
        while self._scheduled and self._scheduled[0].execute_at <= timestamp:
            pmt = heappop(self._scheduled)
            self._pending_by_id.pop(pmt.payment_id, None)
            if pmt.cancelled:
                continue
            try:
                self._do_transfer(
                    pmt.from_id, pmt.to_id, pmt.amount, pmt.execute_at
                )
            except (AccountNotFoundError, InsufficientFundsError):
                # Best-effort: silently drop. Real systems would DLQ.
                pass
        self._current_time = timestamp

    def _do_transfer(
        self, from_id: str, to_id: str, amount: int, timestamp: int
    ) -> None:
        """Internal transfer used by both transfer() and scheduled execution.

        Factored out so the scheduled-payment processor doesn't have to
        re-call _advance_time (which would recurse).
        """
        src = self._get(from_id)
        dst = self._get(to_id)
        if src.account_id == dst.account_id:
            return
        if src.balance < amount:
            raise InsufficientFundsError(from_id)

        src.apply(Transaction(
            str(uuid4()), timestamp, TransactionType.TRANSFER_OUT,
            amount, counterparty=dst.account_id,
        ))
        dst.apply(Transaction(
            str(uuid4()), timestamp, TransactionType.TRANSFER_IN,
            amount, counterparty=src.account_id,
        ))

    # --- L1: accounts and deposits -----------------------------------------

    def add_account(self, timestamp: int, account_id: str) -> None:
        self._advance_time(timestamp)
        if account_id in self._accounts:
            raise DuplicateAccountError(account_id)
        self._accounts[account_id] = Account(account_id=account_id)

    def deposit(self, timestamp: int, account_id: str, amount: int) -> int:
        self._advance_time(timestamp)
        account = self._get(account_id)
        account.apply(Transaction(
            str(uuid4()), timestamp, TransactionType.DEPOSIT, amount,
        ))
        return account.balance

    def get_balance(self, timestamp: int, account_id: str) -> int:
        self._advance_time(timestamp)
        return self._get(account_id).balance

    # --- L2: transfer and ranking ------------------------------------------

    def transfer(
        self, timestamp: int, from_id: str, to_id: str, amount: int
    ) -> None:
        self._advance_time(timestamp)
        self._do_transfer(from_id, to_id, amount, timestamp)

    def top_k_by_volume(
        self, timestamp: int, k: int
    ) -> list[tuple[str, int]]:
        self._advance_time(timestamp)
        ranked = sorted(
            self._accounts.values(),
            key=lambda a: (-a.total_volume(), a.account_id),
        )
        return [(a.account_id, a.total_volume()) for a in ranked[:k]]

    # --- L3: scheduled payments -------------------------------------------

    def schedule_payment(
        self,
        timestamp: int,
        from_id: str,
        to_id: str,
        amount: int,
        execute_at: int,
    ) -> str:
        """Schedule a future transfer. Returns a payment_id."""
        self._advance_time(timestamp)
        if execute_at <= timestamp:
            raise ValueError(
                f"execute_at {execute_at} must be > timestamp {timestamp}"
            )
        # Validate accounts exist NOW. They might disappear by execute_at;
        # _do_transfer handles that gracefully.
        self._get(from_id)
        self._get(to_id)

        payment_id = str(uuid4())
        pmt = ScheduledPayment(
            execute_at=execute_at,
            payment_id=payment_id,
            from_id=from_id,
            to_id=to_id,
            amount=amount,
        )
        heappush(self._scheduled, pmt)
        self._pending_by_id[payment_id] = pmt
        return payment_id

    def cancel_payment(self, timestamp: int, payment_id: str) -> bool:
        """Cancel a pending payment. Returns True if found and cancelled,
        False if already executed or unknown."""
        self._advance_time(timestamp)
        pmt = self._pending_by_id.get(payment_id)
        if pmt is None:
            return False
        pmt.cancelled = True
        return True
