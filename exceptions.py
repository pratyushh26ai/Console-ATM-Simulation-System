"""Custom domain exceptions for ATM operations."""

class ATMError(Exception):
    """Base exception for all ATM-related errors."""


class InsufficientFundsError(ATMError):
    """Raised when a withdrawal exceeds available balance."""


class InvalidAmountError(ATMError):
    """Raised when an operation amount violates validation rules."""


class AuthenticationError(ATMError):
    """Raised when authentication credentials fail validation."""


class AccountNotFoundError(ATMError):
    """Raised when the requested account ID does not exist."""