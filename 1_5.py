# Question 5
# Level 1
#
# Question:
# Define a class which has at least two methods:
#     getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
import string


class Numbers:

    def __init__(self):
        self.string = None

    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())


def main():
    numbers = Numbers()
    numbers.getString()
    numbers.printString()


main()
