'''class Caesar:
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
            return ''.join([self._decode.get(char, char) for char in line])# TODO


key = int(input('Ээъыцмъ фубз:'))
cipher = Caesar(key)
line = input()
while 1>0:
    print(cipher.decode(line))
    line = input()'''
'''for i in range(1,34) :
    key = i
    cipher = Caesar(key)
    print(cipher.decode('Ырпцжцмъ тъмры'))'''




##
##import random
##
##class Monoalphabet:
##    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # TODO
##
##    def __init__(self, keytable):
##        self._encode = dict()
##        self._decode = dict()
##        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
##        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
##
##        lowercase_decode = {x: y for x, y in zip(keytable, self.alphabet)}
##        uppercase_decode = {x.upper(): y.upper() for x, y in zip(keytable, self.alphabet)}
##
##        self._encode = lowercase_code
##        self._encode.update(uppercase_code)
##
##        self._decode = lowercase_decode
##        self._decode.update(uppercase_decode)
##        print(self._decode)
####        print('\n\n\n')
####        print(self._encode)
##        
##
##        
##
##    def encode(self, text):
##        return ''.join([self._encode.get(char, char) for char in text])
##
##    def decode(self, text):
##        return ''.join([self._decode.get(char, char) for char in text])
##
##
####key = Monoalphabet.alphabet[:]
####random.shuffle(key)
####cipher = Monoalphabet(key)
####key = 'гхяезцунтщлсшабэчжюойдрёьыфъмиквп'
####key = input()
##alp = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
##key = 'птхиешцрыязэчджвфгмуеюьоксещйбанл'
##cipher = Monoalphabet(key)
####print(cipher)
##line = input()
##while 1>0 :
##    print(cipher.encode(line))
##    line = input()




class Vigenere:
        alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # TODO

        def __init__(self, keyword):
            self.alphaindex = {ch: index for index, ch in enumerate(self.alphabet)}
            self.key = [self.alphaindex[letter] for letter in keyword.lower()]
##          print(self.alphaindex)
##          print(self.key)
  
        def caesar(self, letter, shift):
            if letter in self.alphaindex:  # строчная буква
                index = (self.alphaindex[letter] + shift)%len(self.alphabet)
                cipherletter = self.alphabet[index]
            elif letter.lower() in self.alphaindex:  # заглавная буква
                cipherletter = self.caesar(letter.lower(), shift).upper()
            else:
                cipherletter = letter
            return cipherletter


        def deceasar(self, letter, shift):
            shift = abs(33 - shift)
            if letter in self.alphaindex:  # строчная буква

                index = (self.alphaindex[letter] + shift)%len(self.alphabet)
                cipherletter = self.alphabet[index]
            elif letter.lower() in self.alphaindex:  # заглавная буква
                cipherletter = self.caesar(letter.lower(), shift).upper()
            else:
                cipherletter = letter
            return cipherletter


        def encode(self, line):
            ciphertext = []
            for i, letter in enumerate(line):
                shift = self.key[i % len(self.key)]
                cipherletter = self.caesar(letter, shift)
                ciphertext.append(cipherletter)

            return ''.join(ciphertext)

        def decode(self, line):
            ciphertext = []
            for i, letter in enumerate(line):
                shift = self.key[i % len(self.key)]
                cipherletter = self.deceasar(letter, shift)
                ciphertext.append(cipherletter)

            return ''.join(ciphertext)

keyword = input('keyword=')
cipher = Vigenere(keyword)

line = input()
while line != '.':
##    print(cipher.encode(line))
    print(cipher.decode(line))
    line = input()



