import re


class N2W_IT:
    def __init__(self):
        self._cardinal_regex = re.compile(r"^[+-]?\d+$")
        self._float_regex = re.compile(r"^[+-]?\d+\.\d+$")
        self._ordinal_regex = re.compile(r"^\+?\d+\°$")

        self._ordinal_roman_regex1 = re.compile(
            "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
        self._ordinal_roman_regex2 = re.compile(
            "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\°$")

        self._zero_word = "zero"

        self._cardinal_words = [
            self._zero_word, "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto",
            "nove", "dieci", "undici", "dodici", "tredici", "quattordici", "quindici",
            "sedici", "diciassette", "diciotto", "diciannove"
        ]

        self._ordinal_words = [
            self._zero_word, "primo", "secondo", "terzo", "quarto", "quinto", "sesto", "settimo",
            "ottavo", "nono", "decimo", "undicesimo", "dodicesimo", "tredicesimo",
            "quattordicesimo", "quindicesimo", "sedicesimo", "diciassettesimo",
            "diciottesimo", "diciannovesimo"
        ]

        self._tens_words = {
            2: "venti", 3: "trenta", 4: "quaranta", 5: "cinquanta",
            6: "sessanta", 7: "settanta", 8: "ottanta", 9: "novanta"
        }

        self._roman_map = {
            "M": 1000, "CM": 900, "D": 500, "CD": 400,
            "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10,
            "IX": 9, "V": 5, "IV": 4, "I": 1
        }

    @staticmethod
    def __adjust_phonetics(text: str) -> str:
        text = text.replace("au", "u")  # trentauno
        text = text.replace("ao", "o")  # settantaotto
        text = text.replace("io", "o")  # ventiotto
        text = text.replace("iu", "u")  # ventiuno

        return text.replace("oo", "o")  # centootto

    def __omitt_if_zero(self, text: str) -> str:
        return "" if text == self._zero_word else text

    def __billions_to_cardinal(self, number: int) -> str:
        billions = number // 1000000000
        millions = number % 1000000000

        prefix = "un miliardo" if billions == 1 else self.__to_cardinal(
            billions) + " miliardi"
        postfix = self.__omitt_if_zero(self.__to_cardinal(millions))

        infix = ", " if " e " in postfix else " e "

        return prefix + infix + postfix

    def __millions_to_cardinal(self, number: int) -> str:
        millions = number // 1000000
        thousands = number % 1000000

        prefix = "un milione" if millions == 1 else self.__to_cardinal(
            millions) + " milioni"
        postfix = self.__omitt_if_zero(self.__to_cardinal(thousands))

        return prefix + " e " + postfix

    def __thousands_to_cardinal(self, number: int) -> str:
        thousands = number // 1000
        hundreds = number % 1000

        prefix = "mille" if thousands == 1 else self.__to_cardinal(
            thousands) + "mila"
        postfix = self.__omitt_if_zero(self.__to_cardinal(hundreds))

        return prefix + postfix

    def __hundreds_to_cardinal(self, number: int) -> str:
        hundreds = number // 100
        tens = number % 100

        prefix = "cento" if hundreds == 1 else self._cardinal_words[hundreds] + "cento"
        postfix = self.__omitt_if_zero(self.__to_cardinal(tens))

        return self.__adjust_phonetics(prefix + postfix)

    def __tens_to_cardinal(self, number: int) -> str:
        tens = number // 10
        units = number % 10

        prefix = self._tens_words[tens]
        postfix = self.__omitt_if_zero(self._cardinal_words[units])

        return self.__adjust_phonetics(prefix + postfix)

    def __to_cardinal(self, number: int) -> str:
        if number < 0:
            return "meno " + self.__to_cardinal(-number)
        elif number < 20:
            return self._cardinal_words[number]
        elif number < 100:
            return self.__tens_to_cardinal(number)
        elif number < 1000:
            return self.__hundreds_to_cardinal(number)
        elif number < 1000000:
            return self.__thousands_to_cardinal(number)
        elif number < 1000000000:
            return self.__millions_to_cardinal(number)
        elif number < 1000000000000:
            return self.__billions_to_cardinal(number)
        else:
            raise ValueError("Numbers over billion are not yet supported.")

    def int_to_cardinal(self, number: int) -> str:
        text = self.__to_cardinal(number)

        words = []
        for word in text.split():
            if word != "tre" and word[-3:] == "tre":
                word = word[:-3] + "tré"
            words.append(word)

        return " ".join(words)

    def float_to_cardinal(self, float_number: float) -> str:
        text = str(float_number).split('.')

        prefix = self.int_to_cardinal(int(text[0]))
        suffix = self.int_to_cardinal(int(text[1]))

        infix = " virgola "

        for char in text[1]:
            if char != "0":
                break
            infix += "zero "

        return prefix + infix + suffix

    def int_to_ordinal(self, number: int) -> str:
        if number < 1:
            raise ValueError("Ordinal numbers cannot be zero or negative.")
        elif number < 20:
            return self._ordinal_words[number]
        else:
            text = self.__to_cardinal(number)

            tens = number % 100
            if tens % 10 != 3 and tens % 10 != 6:
                text = text[:-1]

            if text[-3:] == "mil":
                text += "l"

            return text + "esimo"

    def roman_to_ordinal(self, roman_number: str) -> str:
        # ToDo: Use correct logic.
        if not self._ordinal_roman_regex1.match(roman_number) and \
                not self._ordinal_roman_regex2.match(roman_number):
            raise ValueError("Invalid roman number.")

        result = 0
        index = 0

        for numeral in self._roman_map:
            while roman_number[index:index + len(numeral)] == numeral:
                result += self._roman_map[numeral]
                index += len(numeral)

        return self.int_to_ordinal(result)

    def number_to_words(self, number: str) -> str:
        if not number:
            raise ValueError("Number cannot be null or empty.")
        elif self._cardinal_regex.match(number):
            return self.int_to_cardinal(int(number))
        elif self._float_regex.match(number):
            return self.float_to_cardinal(float(number))
        elif self._ordinal_regex.match(number):
            return self.int_to_ordinal(int(number[:-1]))
        elif self._ordinal_roman_regex1.match(number):
            return self.roman_to_ordinal(number)
        elif self._ordinal_roman_regex2.match(number):
            return self.roman_to_ordinal(number[:-1])
        else:
            raise ValueError("Could not determine number type category.")
