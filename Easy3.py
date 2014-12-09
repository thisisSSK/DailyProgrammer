__author__ = 'thisisSSK'
"""
write a program that can encrypt texts with an alphabetical caesar cipher.
This cipher can ignore numbers, symbols, and whitespace.

for extra credit, add a "decrypt" function to your program!
"""

class Encryptonator(object):
    def __init__(self, given, shift):
        self.original = given.lower()

        self.shift = shift

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        # Encryption dictionary produced with initialization
        self.encryptDict = {
            'a' : alphabet[0-self.shift],
            'b' : alphabet[1-self.shift],
            'c' : alphabet[2-self.shift],
            'd' : alphabet[3-self.shift],
            'e' : alphabet[4-self.shift],
            'f' : alphabet[5-self.shift],
            'g' : alphabet[6-self.shift],
            'h' : alphabet[7-self.shift],
            'i' : alphabet[8-self.shift],
            'j' : alphabet[9-self.shift],
            'k' : alphabet[10-self.shift],
            'l' : alphabet[11-self.shift],
            'm' : alphabet[12-self.shift],
            'n' : alphabet[13-self.shift],
            'o' : alphabet[14-self.shift],
            'p' : alphabet[15-self.shift],
            'q' : alphabet[16-self.shift],
            'r' : alphabet[17-self.shift],
            's' : alphabet[18-self.shift],
            't' : alphabet[19-self.shift],
            'u' : alphabet[20-self.shift],
            'v' : alphabet[21-self.shift],
            'w' : alphabet[22-self.shift],
            'x' : alphabet[23-self.shift],
            'y' : alphabet[24-self.shift],
            'z' : alphabet[25-self.shift],
        }

        self.encrypted = ''
    # produces a new self.encrypted so that multiple calls of this function do not produce incorrect answers
    def encrypt(self):
        newEncrypted = ''
        for letter in self.original:
            if letter.isalpha():
                newEncrypted = newEncrypted + self.encryptDict[letter]

            else:
                self.encrpyted + letter

        self.encrypted = newEncrypted
        print newEncrypted

    # rather than producing a function that decrypts 'decrypted', this simply returns the original input.

    def decrypt(self):
        print self.original
        return self.original

hi = Encryptonator("hello",10)
hi.encrypt()
hi.decrypt()





