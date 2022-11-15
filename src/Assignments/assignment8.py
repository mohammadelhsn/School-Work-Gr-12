#############################################################################
# Author: Mohammad El-Hassan
# Description: Assignemnt #8
# Date Created: 11/15/2022
# Date Modified: 11/14/2022
#############################################################################


class Converter:
    def __init__(self, num: float, convert: str, guess: float):
        self.num = num
        self.convert = convert
        self.guess = round(guess, 2)
        self.KM = 1.609  # multiply
        self.METERS = 1.094  # divide
        self.CM = 2.54  # multiply
        self.KG = 2.205  # divide
        self.L = 3.785  # multiply

    def checkGuess(self, converted):
        if self.guess > converted:
            print("You guessed too high!!")
            print(f"You were off by {self.guess - converted}")
        if self.guess < converted:
            print("You guessed too low!!")
            print(f"You were off by {converted - self.guess}")
        if self.guess == converted:
            print("You guessed it right on! Congrats!")

    def km(self):
        converted = self.num * self.KM

        print(f"{self.num} miles to KM is {converted}km")

        self.checkGuess(converted)

    def meters(self):
        converted = self.num / self.METERS

        print(f"{self.num} yards converted to meters is {converted}m")

        self.checkGuess(converted)

    def cm(self):
        converted = self.num * self.CM

        print(f"{self.num} inches converted to CM is {converted}cm")

        self.checkGuess(converted)

    def kilos(self):
        converted = self.num / self.KG

        print(f"{self.num} pounds converted to kilos is {converted}kg")

        self.checkGuess(converted)

    def litres(self):
        converted = self.num * self.L

        print(f"{self.num} gallons converted to litres is {converted} L")

        self.checkGuess(converted)


while True:
    try:
        num = float(input("What is the number of the thing you want to convert? "))
        convert = int(
            input(
                "What would you like to conver to?\n1) Miles -> KM\n2) Yards -> Meters\n3) Inches -> CM\n4) Pounds -> Kilos\n5) Gallons -> litres\n6) Break"
            )
        )
        guess = float(input("What is your guess "))

        converter = Converter(num, convert, guess)

        if convert == 1:
            converter.km()
        elif convert == 2:
            converter.meters()
        elif convert == 3:
            converter.cm()
        elif convert == 4:
            converter.kilos()
        elif convert == 5:
            converter.litres()
        elif convert == 6:
            break
    except Exception as e:
        print(e)
