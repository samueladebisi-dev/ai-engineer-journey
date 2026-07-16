import csv
import os
import tempfile
import unittest
import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parent.parent / "mini-projects" / "csv_import.py"

spec = importlib.util.spec_from_file_location("csv_import", MODULE_PATH)
csv_import = importlib.util.module_from_spec(spec)
spec.loader.exec_module(csv_import)


class TestCSVImport(unittest.TestCase):

    def test_import(self):
        with tempfile.NamedTemporaryFile(
            mode="w",
            delete=False,
            newline="",
            suffix=".csv",
        ) as temp:

            writer = csv.writer(temp)
            writer.writerow(["name", "category", "amount"])
            writer.writerow(["Lunch", "Food", "2500"])

            filename = temp.name

        expenses = csv_import.import_expenses(filename)

        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]["name"], "Lunch")

        os.remove(filename)


if __name__ == "__main__":
    unittest.main()