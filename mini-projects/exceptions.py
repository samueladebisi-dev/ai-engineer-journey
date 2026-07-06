class ExpenseTrackerError(Exception):
    """Base exception for the Expense Tracker."""


class InvalidExpenseError(ExpenseTrackerError):
    """Raised when an invalid expense is provided."""