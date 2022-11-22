#############################################################################
#Author: Mohammad El-Hassan
#Description: Mini Assingment #13b
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

# Define a function to print out the triangle

def printTriangle(rows: int):

    # base case 

    if rows == 0:
        return

    print("*" * rows)
    printTriangle(rows - 1)


while True:
    try:
        # ask the user how many rows they'd like to print

        rows = int(input("How many rows? "))

        # call the function

        printTriangle(rows)
    except Exception as e:
        print(e)
