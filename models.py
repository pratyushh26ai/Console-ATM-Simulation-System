"""Domain models for accounts and transaction records."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from atm.exceptions import InsufficientFundsError, InvalidAmountError


@dataclass
class Transaction:
    type: str
    amount: float
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class Account:
    def __init__(self, account_id: str, pin: str, name: str, balance: float = 0.0, transactions: List[dict] = None):
        self.account_id = account_id
        self.pin = pin
        self.name = name
        self.balance = float(balance)
        self.transactions: List[Transaction] = [
            Transaction(**t) for t in (transactions or [])
        ]

    def verify_pin(self, pin: str) -> bool:
        return self.pin == pin

    def deposit(self, amount: float, min_limit: float = 1.0, max_limit: float = 100000.0) -> None:
        if amount < min_limit:
            raise InvalidAmountError(f"Deposit amount must be at least {min_limit}.")
        if amount > max_limit:
            raise InvalidAmountError(f"Deposit amount cannot exceed {max_limit}.")

        self.balance += amount
        self.transactions.append(Transaction(type="DEPOSIT", amount=amount))

    def withdraw(self, amount: float, min_limit: float = 1.0, max_limit: float = 50000.0) -> None:
        if amount < min_limit:
            raise InvalidAmountError(f"Withdrawal amount must be at least {min_limit}.")
        if amount > max_limit:
            raise InvalidAmountError(f"Withdrawal amount cannot exceed {max_limit}.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for this withdrawal.")

        self.balance -= amount
        self.transactions.append(Transaction(type="WITHDRAWAL", amount=amount))

    def to_dict(self) -> dict:
        return {
            "pin": self.pin,
            "name": self.name,
            "balance": round(self.balance, 2),
            "transactions": [
                {"type": t.type, "amount": t.amount, "timestamp": t.timestamp}
                for t in self.transactions
            ]
        }