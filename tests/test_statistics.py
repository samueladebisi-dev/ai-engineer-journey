import unittest
import importlib.util
from pathlib import Path

STATS_PATH = Path(__file__).resolve().parent.parent / "mini-projects" / "statistics.py"

spec = importlib.util.spec_from_file_location("statistics", STATS_PATH)
statistics = importlib.util.module_from_spec(spec)
spec.loader.exec_module(statistics)


class TestStatistics(unittest.TestCase):

    def test_average(self):
        self.assertEqual(statistics.average([2,4,6]),4)

    def test_average_empty(self):
        self.assertEqual(statistics.average([]), 0)
        
    def test_maximum(self):
        self.assertEqual(statistics.maximum([10, 5, 20, 8]), 20)

    def test_maximum_empty(self):
        self.assertEqual(statistics.maximum([]), 0)
        
    def test_minimum(self):
        self.assertEqual(statistics.minimum([7, 3, 10]), 3)

    def test_minimum_empty(self):
        self.assertEqual(statistics.minimum([]), 0)
        
    def test_total(self):
        self.assertEqual(statistics.total([5, 10, 15]), 30)

    def test_total_empty(self):
        self.assertEqual(statistics.total([]), 0)
        
    def test_monthly_total(self):
        expenses = [
            {"amount": 100, "category": "Food"},
            {"amount": 200, "category": "Transport"},
        ]

        self.assertEqual(
            statistics.monthly_total(expenses),
            300,
        )


    def test_monthly_total_category(self):
        expenses = [
            {"amount": 100, "category": "Food"},
            {"amount": 200, "category": "Transport"},
            {"amount": 50, "category": "Food"},
        ]

        self.assertEqual(
            statistics.monthly_total(expenses, "Food"),
            150,
        )        

if __name__ == "__main__":
    unittest.main()