__author__ = 'thisisSSK'
"""
create a program that will ask the users name, age, and reddit username.
have it tell them the information back, in the format:

your name is (blank), you are (blank) years old, and your username is (blank)

for extra credit, have the program log this information in a file to be accessed later.
"""
def userInfo():
    name = raw_input("What is your name? ")
    age = raw_input("What is your age? ")
    userName = raw_input("what is your Reddit username? ")

    output = "Your name is " + name + ", you are " + age + " years old, and your username is " + userName

    newFile = open('myInfo.txt', 'w+')
    newFile.write(output)
    newFile.close()

    print output

userInfo()

