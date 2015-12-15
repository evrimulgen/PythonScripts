import string
import random

numberAndLength = []
generatedPasswords = []
alpha = list(string.ascii_letters+string.digits)


def getUserData():
    numberWanted = input("Please enter the number of passwords you want generated: ")
    lengthOfPasswords = input("Please enter the length desired for your passwords: ")
    numberAndLength.append(numberWanted)
    numberAndLength.append(lengthOfPasswords)


def makePasswords():
    passwordsWanted = int(numberAndLength[0])
    lengthWanted = int(numberAndLength[1])
    for passwordsCreated in range(passwordsWanted):
        created = ''.join(random.choice(alpha) for _ in range(lengthWanted))
        generatedPasswords.append(created)


def printPasswords():
    i = 1
    print("Your generated passwords are: ")
    for gen in generatedPasswords:
        print(str(i) + str(')') + gen)
        i += 1

if __name__ == '__main__':
    getUserData()
    makePasswords()
    printPasswords()