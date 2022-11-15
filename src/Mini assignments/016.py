#############################################################################
# Author: Mohammad El-Hassan
# Description: Mini Assingment #16
# Date Created: 11/14/2022
# Date Modified: 11/14/2022
#############################################################################

class Calculator:
    def __init__(self, x, y) -> None:
        self.x = int(x)
        self.y = int(y)

    def sum(self):
        return self.x + self.y

    def subtract(self):
        return self.y - self.x

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.y / self.x

while True:
    try:
        nums = input("Enter 2 numbers seperated by a space").split()

        calculator = Calculator(nums[0], nums[1])

        q = False
        while q != True:
            operation = input("Which operation would you like to perform (+,-,/,*,q)? ")

            if operation == "q":
                q == False
                continue

            if operation == "+":
                print(calculator.sum())
                continue
            if operation == "-":
                print(calculator.subtract())
                continue
            if operation == "*":
                print(calculator.multiply())
                continue
            if operation == "/":
                print(calculator.divide())
                continue

    except Exception as e:
        print(e)
