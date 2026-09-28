"""Data access layer for loading and persisting accounts."""

import json
import os
from typing import Dict, Optional
from atm.exceptions import AccountNotFoundError
from atm.models import Account


class AccountRepository:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        directory = os.path.dirname(self.filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump({}, file, indent=2)

    def load_accounts(self) -> Dict[str, Account]:
        with open(self.filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
        return {
            acc_id: Account(
                account_id=acc_id,
                pin=payload["pin"],
                name=payload["name"],
                balance=payload["balance"],
                transactions=payload.get("transactions", [])
            )
            for acc_id, payload in data.items()
        }

    def save_accounts(self, accounts: Dict[str, Account]) -> None:
        serialized = {acc_id: acc.to_dict() for acc_id, acc in accounts.items()}
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(serialized, file, indent=2)

    def get_by_id(self, account_id: str) -> Account:
        accounts = self.load_accounts()
        if account_id not in accounts:
            raise AccountNotFoundError(f"Account '{account_id}' does not exist.")
        return accounts[account_id]

    def update_account(self, account: Account) -> None:
        accounts = self.load_accounts()
        accounts[account.account_id] = account
        self.save_accounts(accounts)