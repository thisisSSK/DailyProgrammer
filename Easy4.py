__author__ = 'thisisSSK'
"""
You're challenge for today is to create a random password generator!

For extra credit, allow the user to specify the amount of passwords to generate.

For even more extra credit, allow the user to specify the length of the strings he wants to generate!
"""

import random
import string


def generatePassword(numPasswords, length):
    if numPasswords != 0:
        posChars = string.printable
        password = ''
        for index in range(length):
            password = password + random.choice(posChars)
        print password
        print "--------------------------------------------"
        generatePassword(numPasswords-1,length)


generatePassword(100, 1000)