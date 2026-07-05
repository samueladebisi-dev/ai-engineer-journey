import unittest


class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(10 + 5, 15)

    def test_subtract(self):
        self.assertEqual(10 - 5, 5)

    def test_multiply(self):
        self.assertEqual(5 * 4, 20)


if __name__ == "__main__":
    unittest.main()