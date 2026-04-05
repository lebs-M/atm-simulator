import json
import os
from datetime import datetime

DEFAULT_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "account.json")


class Account:

    def __init__(self, data_path=DEFAULT_DATA_PATH): 
        self.data_path = data_path
        self._load()

    def _load(self):
        if os.path.exists(self.data_path):
            with open(self.data_path, "r") as f:
                data = json.load(f)
            self.balance = data.get("balance", 0.0)
            self.transactions = data.get("transactions", [])
        else:
            self.balance = 0.0
            self.transactions = []
            self._save()

    def _save(self):
        """Persist account data to the JSON file."""
        os.makedirs(os.path.dirname(self.data_path), exist_ok=True)
        with open(self.data_path, "w") as f:
            json.dump(
                {"balance": self.balance, "transactions": self.transactions},
                f,
                indent=4,
            )

    def _record(self, type_, amount, note=""):
        """Record a transaction with a timestamp."""
        self.transactions.append({
            "type": type_,
            "amount": amount,
            "note": note,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })

    def get_balance(self):
        """Return the current balance."""
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit amount must be greater than zero."
        self.balance += amount
        self._record("DEPOSIT", amount)
        self._save()
        return True, f"Successfully deposited R{amount:,.2f}."

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be greater than zero."
        if amount > self.balance:
            return False, "Insufficient funds."
        self.balance -= amount
        self._record("WITHDRAWAL", amount)
        self._save()
        return True, f"Successfully withdrew R{amount:,.2f}."

    def get_history(self):
        return self.transactions
