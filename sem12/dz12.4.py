import unittest


class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        self._encode = dict()
        self._decode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()

            decoded = self.alphabet[(i - key) % len(self.alphabet)]
            self._decode[letter] = decoded
            self._decode[letter.upper()] = decoded.upper()

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        return ''.join([self._decode.get(char, char) for char in line])


key = input('Введите ключ:')


class TestType(unittest.TestCase):
    def test_Type(self):
        self.assertEqual(key.isdigit(), True, "key should be digit")


if __name__ == "__main__":
    unittest.main()
key = int(key)
cipher = Caesar(key)
line = input()
while 1 > 0:
    print(cipher.decode(line))
    line = input()
