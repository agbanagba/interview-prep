from dataclasses import dataclass, field
from enum import Enum
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
    counterparty: Optional[str] = None  # None for deposit/withdraw


@dataclass
class Account:
    account_id: str
    balance: int = 0
    log: list[Transaction] = field(default_factory=list)

    # Which transaction types are credits (add to balance) vs debits.
    # Centralising this here means apply() doesn't have to know about
    # each new type — only this set does.
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
        """Sum of all transaction amounts ever applied. Used for ranking."""
        return sum(t.amount for t in self.log)

    def transaction_count(self) -> int:
        return len(self.log)


class AccountNotFoundError(Exception): pass
class DuplicateAccountError(Exception): pass
class InsufficientFundsError(Exception): pass


class BankingSystem:
    def __init__(self):
        self._accounts: dict[str, Account] = {}

    def add_account(self, timestamp: int, account_id: str) -> None:
        if account_id in self._accounts:
            raise DuplicateAccountError(account_id)
        self._accounts[account_id] = Account(account_id=account_id)

    def deposit(self, timestamp: int, account_id: str, amount: int) -> int:
        account = self._get(account_id)
        account.apply(Transaction(
            str(uuid4()), timestamp, TransactionType.DEPOSIT, amount,
        ))
        return account.balance

    def transfer(
        self,
        timestamp: int,
        from_id: str,
        to_id: str,
        amount: int,
    ) -> None:
        """Atomic transfer between two accounts.

        Atomic = both legs succeed or neither. We check the balance
        first; if it passes, both writes proceed. Single-threaded so
        no actual transaction needed yet.
        """
        src = self._get(from_id)
        dst = self._get(to_id)
        if src.account_id == dst.account_id:
            return  # self-transfer no-op
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

    def get_balance(self, timestamp: int, account_id: str) -> int:
        return self._get(account_id).balance

    def top_k_by_volume(
        self, timestamp: int, k: int
    ) -> list[tuple[str, int]]:
        """Top-K accounts by total transaction volume.

        Tie-break by account_id ascending for determinism.

        Complexity: O(n log n) sort. For large n with small k, a heap
        gives O(n log k) — mention this in conversation, don't pre-build.
        """
        ranked = sorted(
            self._accounts.values(),
            key=lambda a: (-a.total_volume(), a.account_id),
        )
        return [(a.account_id, a.total_volume()) for a in ranked[:k]]

    def top_k_by_count(
        self, timestamp: int, k: int
    ) -> list[tuple[str, int]]:
        """Alternative interpretation: rank by transaction count."""
        ranked = sorted(
            self._accounts.values(),
            key=lambda a: (-a.transaction_count(), a.account_id),
        )
        return [(a.account_id, a.transaction_count()) for a in ranked[:k]]

    def _get(self, account_id: str) -> Account:
        if account_id not in self._accounts:
            raise AccountNotFoundError(account_id)
        return self._accounts[account_id]

