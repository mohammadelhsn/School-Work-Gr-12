#############################################################################
#Author: Mohammad El-Hassan
#Description: Assignemnt #1
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

while True:
    try:
        # get the input from the user (first number, second number and operation)
        
        num1 = int(input("What is your first number? "))
        num2 = int(input("What is your second number? "))
        operation = input("What is operation would you like to try? ")

        # define the functions that are going to be used to calculate
        add = lambda a, b: a + b
        subtract = lambda a, b: a - b
        multiply = lambda a, b: a * b
        divide = lambda a, b: a / b

        # if the operation is add
        if operation.lower() == "add":
            print(add(num1, num2))
            continue

        # if the operation is subtract

        if operation.lower() == "sub":
            print(subtract(num1, num2))
            continue

        # if the operation is multiply

        if operation.lower() == "multiply":
            print(multiply(num1, num2))
            continue

        # if the operation is divide
        if operation.lower() == "divide":
            print(divide(num1, num2))
            continue

        # else it is an invalid choice

        else:
            raise Exception("Invalid Num / Invalid operation")
    except Exception as e:
        # Print error the console for debugging and cotinue

        print(e)
        continue
