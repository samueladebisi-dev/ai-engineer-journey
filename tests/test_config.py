import unittest
import importlib.util
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "mini-projects" / "config.py"

spec = importlib.util.spec_from_file_location("config", CONFIG_PATH)
config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(config)


class TestConfig(unittest.TestCase):

    def test_version_exists(self):
        self.assertTrue(hasattr(config, "VERSION"))


if __name__ == "__main__":
    unittest.main()