import unittest
from expense_manager import ExpenseManager


class TestExpenseManager(unittest.TestCase):

    def test_add(self):
        manager = ExpenseManager([])

        manager.add(
            {
                "name": "Food",
                "category": "Food",
                "amount": 100,
            }
        )

        self.assertEqual(len(manager.all()), 1)


if __name__ == "__main__":
    unittest.main()