from fileinput import filename
import json
import tempfile
import unittest
from pathlib import Path
import importlib.util

UTILS_PATH = Path(__file__).resolve().parent.parent / "mini-projects" / "utils.py"

spec = importlib.util.spec_from_file_location("utils", UTILS_PATH)
utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(utils)


class TestJsonUtils(unittest.TestCase):

    def test_save_and_load_json(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            filename = temp.name

        data = [
            {"name": "Transport", "amount": 2000}
        ]

        utils.save_json(filename, data)

        loaded = utils.load_json(filename)

        self.assertEqual(data, loaded)
     
    def test_save_empty_list(self):
        import tempfile

        with tempfile.NamedTemporaryFile(delete=False) as temp:
            filename = temp.name

        utils.save_json(filename, [])

        loaded = utils.load_json(filename)

        self.assertEqual([], loaded)
        
    def test_load_missing_file(self):
        data = utils.load_json("file_that_does_not_exist.json")
        self.assertEqual(data, [])


if __name__ == "__main__":
    unittest.main()