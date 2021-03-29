import unittest

from n2w_it import N2W_IT


class Test_N2W_IT(unittest.TestCase):
    def setUp(self):
        self._instance = N2W_IT()

    def test_int_to_cardinal(self):
        value1 = self._instance.int_to_cardinal(987654321063)
        value2 = "novecentottantasette miliardi, seicentocinquantaquattro milioni e trecentoventunomilasessantatré"

        self.assertEqual(value1, value2)

    def test_float_to_cardinal(self):
        value1 = self._instance.float_to_cardinal(156.0023868)
        value2 = "centocinquantasei virgola zero zero ventitremilaottocentosessantotto"

        self.assertEqual(value1, value2)

    def test_int_to_ordinal(self):
        value1 = self._instance.int_to_ordinal(137)
        value2 = "centotrentasettesimo"

        self.assertEqual(value1, value2)

    def test_roman_to_ordinal(self):
        value1 = self._instance.roman_to_ordinal("DCLXII")
        value2 = "seicentosessantaduesimo"

        self.assertEqual(value1, value2)

    def test_number_to_words(self):
        function = self._instance.number_to_words
        value = "1000000000000"

        self.assertRaises(ValueError, function, value)


if __name__ == "__main__":
    unittest.main()
