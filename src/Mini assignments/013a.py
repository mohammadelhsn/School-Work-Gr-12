"""
Create a program that takes the values of a number and adds them together.  For example 101 would be 1 + 0 + 1 = 2.  Use recursion to complete along with functions

HINT :  and you will need to use both Modulus and Floor to work out the answers. 

It is a math problem and a little tricky.

If you can't figure it out, highlight the code below and try again.

def sumnumber(number):

    if number == 0:

        return 0

    else:

        return (number%10) + sumnumber(number//10)

number = int(input("what is the number"))

print(sumnumber(number))
"""


while True:
    try:
        num = input("What is the number? ")

        num = list(num)
    except Exception as e:
        print(e)
