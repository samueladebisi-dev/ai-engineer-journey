import csv
import os
import tempfile
import unittest
import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parent.parent / "mini-projects" / "csv_export.py"

spec = importlib.util.spec_from_file_location("csv_export", MODULE_PATH)
csv_export = importlib.util.module_from_spec(spec)
spec.loader.exec_module(csv_export)


class TestCSVExport(unittest.TestCase):

    def test_export(self):
        data = [
            {
                "name": "Food",
                "category": "Feeding",
                "amount": 1500
            }
        ]

        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp:
            filename = temp.name

        csv_export.export_expenses(data, filename)

        with open(filename, newline="", encoding="utf-8") as file:
            rows = list(csv.DictReader(file))

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["name"], "Food")

        os.remove(filename)


if __name__ == "__main__":
    unittest.main()