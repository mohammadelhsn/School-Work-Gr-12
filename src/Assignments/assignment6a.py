#############################################################################
#Author: Mohammad El-Hassan
#Description: Assignemnt #6a
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

def displayTotal(i=0, total=0):
    try:
        m = int(input("Enter a number of hit enter"))

        total += m
        print(total)
        displayTotal(m, total)

    except Exception as e:
        print(total)
        displayTotal(i, total)


while True:
    displayTotal()
