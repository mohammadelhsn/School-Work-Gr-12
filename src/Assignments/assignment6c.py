#############################################################################
#Author: Mohammad El-Hassan
#Description: Assignemnt #6c
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################


def beginning(length, char="*"):
    return f"{char} " * length

def middle(length, char="*"):
    mid = (length - 2) * "  "
    return f"{char} " + f"{mid}" + f"{char}"

def draw(length: int, char="*", row=0):
    if (row == length): 
        print(beginning(length, char))
        return
    if (row == 0): 
        print(beginning(length, char))
        row = row + 1
        return draw(length, char, row)
    else: 
        print(middle(length, char))
        row = row + 1
        return draw(length, char, row)


while True: 
    try: 
        length = int(input("What is the length of the square? "))

        draw(length)

        size = float(input("Use a decimal if you'd like to make it smaller, use a whole number if you'd like to make it bigger "))

        s = int(length * size) 

        draw(s)
    except Exception as e:
        print(e) 
