#############################################################################
#Author: Mohammad El-Hassan
#Description: Assignemnt #3b
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

import math


def pyth(a: int, b: int):
    a = math.pow(a, 2)
    b = math.pow(b, 2)
    total = a + b
    return math.sqrt(total)


while True:
    try:
        a = int(input("What is the length of side 1? "))
        b = int(input("What is the length of side 2? "))
        answer = pyth(a, b)
        print(
            f"The hypotenuse of a triangle with a side lenght of {a} and another side length of {b} is {answer}"
        )
        again = int(input("Would you like to paly again?\n1) Yes\n2) No\n"))
        if again == 1:
            continue
        if again == 2:
            break
        else:
            continue
    except Exception as e:
        print(e)
        continue
