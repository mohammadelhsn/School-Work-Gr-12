#############################################################################
#Author: Mohammad El-Hassan
#Description: Mini Assingment #2
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

# Import the random module for the generator
import random

while True:
    try:
        # Taking in the user input for the start and end of the range

        start = int(input("Where would you like the range to start from? "))
        end = int(input("Where would you like the range to end? "))

        # Check if the starting range is higher than the ending range. 

        if end < start:
            raise Exception("The end lower is higher than the beginning number")

        # Define the generator function

        def generator(start: int, end: int):
            return random.randrange(start, end, 2)

        # Call the function and print the result 

        print(generator(start, end))

    except Exception as e:
        print(e)
        continue
