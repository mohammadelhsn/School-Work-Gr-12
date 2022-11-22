#############################################################################
# Author: Mohammad El-Hassan
# Description: Mini Assingment #13c
# Date Created: 11/12/2022
# Date Modified: 11/12/2022
#############################################################################


def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)


try:
    # get the user input for 2 numbers

    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    # print the result

    print("The GCF of", a, "and", b, "is", gcf(a, b))
except Exception as e:
    print(e)
