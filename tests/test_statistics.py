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

if __name__ == "__main__":
    unittest.main()