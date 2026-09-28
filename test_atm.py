import pytest
from atm.exceptions import InsufficientFundsError, InvalidAmountError
from atm.models import Account


@pytest.fixture
def sample_account():
    return Account(account_id="9999", pin="0000", name="Test User", balance=1000.0)


def test_successful_deposit(sample_account):
    sample_account.deposit(500.0, min_limit=10.0, max_limit=5000.0)
    assert sample_account.balance == 1500.0
    assert len(sample_account.transactions) == 1
    assert sample_account.transactions[0].type == "DEPOSIT"


def test_deposit_below_min_raises_error(sample_account):
    with pytest.raises(InvalidAmountError):
        sample_account.deposit(5.0, min_limit=10.0, max_limit=5000.0)


def test_deposit_above_max_raises_error(sample_account):
    with pytest.raises(InvalidAmountError):
        sample_account.deposit(6000.0, min_limit=10.0, max_limit=5000.0)


def test_successful_withdrawal(sample_account):
    sample_account.withdraw(400.0, min_limit=50.0, max_limit=1000.0)
    assert sample_account.balance == 600.0
    assert len(sample_account.transactions) == 1
    assert sample_account.transactions[0].type == "WITHDRAWAL"


def test_withdrawal_insufficient_funds(sample_account):
    with pytest.raises(InsufficientFundsError):
        sample_account.withdraw(1200.0, min_limit=50.0, max_limit=2000.0)


def test_pin_verification(sample_account):
    assert sample_account.verify_pin("0000") is True
    assert sample_account.verify_pin("1111") is False