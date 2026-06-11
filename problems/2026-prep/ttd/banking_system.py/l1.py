from dataclasses import dataclass, field
from enum import Enum
from uuid import uuid4


class TransactionType(Enum):
    DEPOSIT = "deposit"


@dataclass(frozen=True)
class Transaction:
    txn_id: str
    timestamp: int
    type: TransactionType
    amount: int


@dataclass
class Account:
    account_id: str
    balance: int = 0
    log: list[Transaction] = field(default_factory=list)

    def apply(self, txn: Transaction) -> None:
        """Central place to update balance and log together — avoids
        drift between the two."""
        self.balance += txn.amount
        self.log.append(txn)


class AccountNotFoundError(Exception): pass
class DuplicateAccountError(Exception): pass


class BankingSystem:
    def __init__(self):
        self._accounts: dict[str, Account] = {}

    def add_account(self, timestamp: int, account_id: str) -> None:
        if account_id in self._accounts:
            raise DuplicateAccountError(account_id)
        self._accounts[account_id] = Account(account_id=account_id)

    def deposit(self, timestamp: int, account_id: str, amount: int) -> int:
        """Deposit and return new balance."""
        account = self._get(account_id)
        account.apply(Transaction(
            txn_id=str(uuid4()),
            timestamp=timestamp,
            type=TransactionType.DEPOSIT,
            amount=amount,
        ))
        return account.balance

    def get_balance(self, timestamp: int, account_id: str) -> int:
        return self._get(account_id).balance

    def _get(self, account_id: str) -> Account:
        if account_id not in self._accounts:
            raise AccountNotFoundError(account_id)
        return self._accounts[account_id]

