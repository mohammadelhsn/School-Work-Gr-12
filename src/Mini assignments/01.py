#############################################################################
#Author: Mohammad El-Hassan
#Description: Mini Assingment #1
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

while True:
    try:
        # Get the user input

        num = int(input("What is your number"))

        # Define a function to do math and output the result to the console

        def doMath(num):
            print(f"Added your number {num} to 10 which is equal to {num+10}")
            print(f"Multiplied your nunber {num} by 10 which is equal to {num*10}")
            print(f"Divided your number {num} by 10 which is equal to {num/10}")

        # Call the function

        doMath(num)
    except Exception as e:
        # Print the error to the console for debugging

        print(e)

        # Continue the loop

        continue