import unittest
from n2w_it import N2W_IT


class Test_N2W_IT(unittest.TestCase):
    """Tests for `n2w_it` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

        self._instance = N2W_IT()

    def test_int_to_cardinal(self):
        """Test something."""

        self.assertEqual(self._instance.int_to_cardinal(5), "cinque")

    def test_float_to_cardinal(self):
        """Test something."""

        self.assertEqual(self._instance.float_to_cardinal(
            5.5), "cinque virgola cinque")

    def test_int_to_ordinal(self):
        """Test something."""

        self.assertEqual(self._instance.int_to_ordinal(5), "quinto")

    def test_roman_to_ordinal(self):
        """Test something."""

        self.assertEqual(self._instance.roman_to_ordinal("V"), "quinto")


if __name__ == "__main__":
    unittest.main()
