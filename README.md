```markdown
# Console ATM Simulation System

A lightweight, object-oriented console application written in Python that simulates essential automated teller machine (ATM) operations, including real-time balance inquiries, deposits, and withdrawals with robust input validation.

---

## 📌 Overview

The **Console ATM Simulation System** models standard banking kiosk interactions in a terminal interface. The project implements a clean separation of concerns by splitting responsibilities across two core classes:
- **`ATM` (Model):** Encapsulates balance state and enforces core banking business logic (e.g., non-negative transactions, non-overdraft withdrawals).
- **`ATMController` (Controller / View):** Manages terminal interaction, user input sanitization, menu loops, and friendly error feedback.

---

## ✨ Features

- **Check Balance:** View current account funds at any time.
- **Deposit Funds:** Add money to the account balance with positive-amount validation.
- **Withdraw Funds:** Deduct funds safely with automatic verification to prevent overdrafts.
- **Error Handling & Input Validation:**
  - Guards against non-numeric inputs without crashing.
  - Rejects zero and negative amounts.
  - Surfaces clean, user-friendly exception messages on invalid operations.
- **Looping Terminal UI:** Interactive menu that runs continuously until the user chooses to exit.

---

## 🛠️ Technologies & Tools Used

- **Language:** Python 3.8+
- **Standard Library:** `unittest` (for unit testing, zero third-party dependencies required)
- **Environment:** Compatible with Linux, macOS, and Windows command prompts / terminals

---

## 🚀 Installation & Running

### 1. Prerequisites
Ensure Python 3 is installed on your system. Verify by running:
```bash
python --version
# or
python3 --version

```

### 2. Clone the Repository

```bash
git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
cd <your-repo-name>

```

### 3. Run the Application

Execute the Python script directly from your terminal:

```bash
python atm.py
# or
python3 atm.py

```

---

## 🧪 Testing

The underlying business logic (`ATM` class) can be verified using Python's built-in `unittest` runner.

### Create a Test File (`test_atm.py`)

Save the following test suite in the same directory:

```python
import unittest
from atm import ATM

class TestATM(unittest.TestCase):
    def setUp(self):
        self.atm = ATM()

    def test_initial_balance(self):
        self.assertEqual(self.atm.check_balance(), 0)

    def test_deposit_valid(self):
        self.atm.deposit(500)
        self.assertEqual(self.atm.check_balance(), 500)

    def test_deposit_negative_raises_error(self):
        with self.assertRaises(ValueError):
            self.atm.deposit(-100)

    def test_deposit_zero_raises_error(self):
        with self.assertRaises(ValueError):
            self.atm.deposit(0)

    def test_withdraw_valid(self):
        self.atm.deposit(1000)
        self.atm.withdraw(400)
        self.assertEqual(self.atm.check_balance(), 600)

    def test_withdraw_insufficient_funds(self):
        self.atm.deposit(200)
        with self.assertRaises(ValueError):
            self.atm.withdraw(500)

    def test_withdraw_negative_raises_error(self):
        with self.assertRaises(ValueError):
            self.atm.withdraw(-50)

if __name__ == '__main__':
    unittest.main()

```

### Run the Tests

Execute the tests via:

```bash
python -m unittest test_atm.py

```

---

## 📸 Screenshots

*(Replace these image paths with your actual repository screenshots stored in an `assets/` or `images/` directory).*

### Main Menu & Deposit

```text
Welcome to the ATM!
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Please choose an option: 2
Enter the amount to deposit: 1500
Successfully deposited ₹1500.0.

```

### Balance Inquiry & Withdrawal

```text
Welcome to the ATM!
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Please choose an option: 1
Your current balance is: ₹1500.0

Welcome to the ATM!
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Please choose an option: 3
Enter the amount to withdraw: 500
Successfully withdrew ₹500.0.

```

---

```
