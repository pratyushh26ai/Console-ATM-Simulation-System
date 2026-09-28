"""Application orchestrator and CLI boundary layer."""

import json
from atm.exceptions import ATMError, AuthenticationError
from atm.models import Account
from atm.repository import AccountRepository


class ATMController:
    def __init__(self, config_path: str = "config.json"):
        with open(config_path, "r", encoding="utf-8") as file:
            self.config = json.load(file)

        self.repo = AccountRepository(self.config["data_file_path"])
        self.currency = self.config.get("currency_symbol", "₹")
        self.current_account: Account | None = None

    def _prompt_float(self, prompt: str) -> float:
        while True:
            raw = input(prompt).strip()
            try:
                val = float(raw)
                return val
            except ValueError:
                print("Invalid input. Please enter a valid numerical value.")

    def login(self) -> bool:
        print("\n--- Card Authentication ---")
        acc_id = input("Enter Account Number: ").strip()
        pin = input("Enter 4-Digit PIN: ").strip()

        try:
            account = self.repo.get_by_id(acc_id)
            if not account.verify_pin(pin):
                raise AuthenticationError("Invalid PIN supplied.")
            self.current_account = account
            print(f"Authentication successful. Welcome, {account.name}!")
            return True
        except ATMError as err:
            print(f"Error: {err}")
            return False

    def check_balance(self) -> None:
        print(f"\nYour current balance: {self.currency}{self.current_account.balance:,.2f}")

    def deposit(self) -> None:
        amount = self._prompt_float(f"\nEnter deposit amount ({self.currency}): ")
        try:
            self.current_account.deposit(
                amount,
                min_limit=self.config["min_deposit"],
                max_limit=self.config["max_deposit"]
            )
            self.repo.update_account(self.current_account)
            print(f"Deposit successful. Updated balance: {self.currency}{self.current_account.balance:,.2f}")
        except ATMError as err:
            print(f"Transaction failed: {err}")

    def withdraw(self) -> None:
        amount = self._prompt_float(f"\nEnter withdrawal amount ({self.currency}): ")
        try:
            self.current_account.withdraw(
                amount,
                min_limit=self.config["min_withdrawal"],
                max_limit=self.config["max_withdrawal"]
            )
            self.repo.update_account(self.current_account)
            print(f"Withdrawal successful. Remaining balance: {self.currency}{self.current_account.balance:,.2f}")
        except ATMError as err:
            print(f"Transaction failed: {err}")

    def print_mini_statement(self) -> None:
        print(f"\n--- Mini Statement for {self.current_account.name} ---")
        recent = self.current_account.transactions[-5:]
        if not recent:
            print("No transactions recorded yet.")
            return

        for t in reversed(recent):
            print(f"[{t.timestamp[:19]}] {t.type:<12} | {self.currency}{t.amount:,.2f}")
        print(f"Current Balance: {self.currency}{self.current_account.balance:,.2f}")

    def run(self) -> None:
        print("=" * 40)
        print("          AUTOMATED TELLER MACHINE         ")
        print("=" * 40)

        while not self.current_account:
            if not self.login():
                retry = input("Try again? (y/n): ").strip().lower()
                if retry != "y":
                    print("Exiting system. Have a good day.")
                    return

        while True:
            print("\n--- Main Menu ---")
            print("1. Check Balance")
            print("2. Deposit Funds")
            print("3. Withdraw Funds")
            print("4. Mini Statement")
            print("5. Eject Card & Exit")

            choice = input("Select an option (1-5): ").strip()
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.print_mini_statement()
            elif choice == "5":
                print(f"\nCard returned. Thank you for banking with us, {self.current_account.name}!")
                break
            else:
                print("Invalid option selected. Please choose between 1 and 5.")