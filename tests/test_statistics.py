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


if __name__ == "__main__":
    unittest.main()