"""
Mini-assignment 15

Without looking at what you just coded, create a class and method.  Within the class, pass a value through it (remember, similar to functions).  

Create the class

Create a method within the class

Return a value

Create an object / instance

Print out that value

Try this on your own without looking at your previous code, it will help you become a better programmer.
"""
import random


class Generator:
    def __init__(self):
        pass

    def method(self,start=1, end=50):
        return random.randint(start, end)


# Create the instance of the above class

a = Generator()

print(a.method())
