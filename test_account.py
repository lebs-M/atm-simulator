import pytest
import os
import json
import tempfile
from account import Account


@pytest.fixture
def temp_account():
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as f: #clean JSON file for each test
        json.dump({"balance": 1000.0, "transactions": []}, f)
        path = f.name
    account = Account(data_path=path)
    yield account
    os.unlink(path)


class TestDeposit:
    def test_valid_deposit(self, temp_account):
        success, msg = temp_account.deposit(500)
        assert success is True
        assert temp_account.get_balance() == 1500.0

    def test_zero_deposit_rejected(self, temp_account):
        success, _ = temp_account.deposit(0)
        assert success is False

    def test_negative_deposit_rejected(self, temp_account):
        success, _ = temp_account.deposit(-100)
        assert success is False

    def test_deposit_recorded_in_history(self, temp_account):
        temp_account.deposit(200)
        history = temp_account.get_history()
        assert any(t["type"] == "DEPOSIT" and t["amount"] == 200 for t in history)


class TestWithdraw:
    def test_valid_withdrawal(self, temp_account):
        success, msg = temp_account.withdraw(400)
        assert success is True
        assert temp_account.get_balance() == 600.0

    def test_insufficient_funds(self, temp_account):
        success, msg = temp_account.withdraw(9999)
        assert success is False
        assert "Insufficient" in msg

    def test_zero_withdrawal_rejected(self, temp_account):
        success, _ = temp_account.withdraw(0)
        assert success is False

    def test_negative_withdrawal_rejected(self, temp_account):
        success, _ = temp_account.withdraw(-50)
        assert success is False

    def test_withdrawal_recorded_in_history(self, temp_account):
        temp_account.withdraw(100)
        history = temp_account.get_history()
        assert any(t["type"] == "WITHDRAWAL" and t["amount"] == 100 for t in history)

    def test_exact_balance_withdrawal(self, temp_account):
        success, _ = temp_account.withdraw(1000)
        assert success is True
        assert temp_account.get_balance() == 0.0


class TestBalance:
    def test_initial_balance(self, temp_account):
        assert temp_account.get_balance() == 1000.0

    def test_balance_after_deposit_and_withdrawal(self, temp_account):
        temp_account.deposit(500)
        temp_account.withdraw(200)
        assert temp_account.get_balance() == 1300.0


class TestPersistence:
    def test_data_saves_to_file(self, temp_account):
        temp_account.deposit(250)
        with open(temp_account.data_path, "r") as f:
            data = json.load(f)
        assert data["balance"] == 1250.0

    def test_data_loads_from_file(self, temp_account):
        temp_account.deposit(300)
        reloaded = Account(data_path=temp_account.data_path)
        assert reloaded.get_balance() == 1300.0
