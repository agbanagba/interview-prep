from dataclasses import dataclass, field
from enum import Enum
from uuid import uuid4
from typing import Optional, List

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
    execute_at: int
    payment_id: str = field(comapre=False)
    from_id: str = field(compare=False)
    to_id: str = field(compare=False)
    amount: int = field(compare=False)
    cancelled: bool = field(default=False, compare=False)


class DuplicateAccountError(Exception): pass
class AccountNotFoundError(Exception): pass
class InsufficientFundsError(Exception): pass
class TimeWentBackwardsError(Exception): pass

class BankingSystem:

    def __init__(self):
        self._accounts: dict[str, Account] = {}
        self._scheduled: List[ScheduledPayment] = []
        self._pending_by_id: dict[str, ScheduledPayment] = {}
        self._current_time: int = 0

    def add_acocunt(self, account_id: str) -> None:
        if account_id in self._accounts:
            raise DuplicateAccountError(account_id)
        self._accounts[account_id] = Account(account_id=account_id)

    def deposit(self, timestamp: int, account_id: str, amount: int) -> int:
        account = self._get(account_id)
        account.apply(
            Transaction(
                txn_id=str(uuid4()), 
                timestamp=timestamp,
                type=TransactionType.DEPOSIT,
                amount=amount,
            )
        )
        return account.balance
    
    def get_balance(self, timestamp: int, account_id: str) -> int:
        return self._get(account_id).balance
    
    def top_k_by_volume(self, k: int) -> List[tuple[str, int]]:
        ranked = sorted(
            self._accounts.values(),
            key=lambda a: (-a.total_volume(), a.account_id)
        )
        return [(a.account_id, a.total_volume()) for a in ranked[:k]]
    
    def top_k_by_count(self, k: int) -> List[tuple[str, int]]:
        pairs = [(a.transanction_count(), a.account_id) for a in self._accounts.values()]
        ranked = sorted(pairs, key=lambda x: x[0], reverse=True)
        return [(a.account_id, a.transaction_count()) for a in ranked[:k]]        


    def _get(self, account_id: str) -> Account:
        if account_id not in self._accounts:
            raise AccountNotFoundError(account_id)
        return self._accounts[account_id]
    
    
    def transfer(self, timestamp: int, from_id: str, to_id: str, amount: int) -> None:
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
