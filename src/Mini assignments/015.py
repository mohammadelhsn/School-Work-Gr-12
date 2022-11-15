#############################################################################
# Author: Mohammad El-Hassan
# Description: Mini Assingment #15
# Date Created: 11/12/2022
# Date Modified: 11/12/2022
#############################################################################

import random


class Generator:
    def __init__(self):
        pass

    def method(self, start=1, end=50):
        return random.randint(start, end)


# Create the instance of the above class

a = Generator()

print(a.method())
