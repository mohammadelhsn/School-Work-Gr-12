#############################################################################
#Author: Mohammad El-Hassan
#Description: Mini Assingment #14
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

class New:
    inv = "gold"

    def __init__(self) -> None:
        pass

    def add(self, n1=40, n2=30):
        return n1 + n2


i = New()
print(f"Here is the amount of {i.inv} I have: {i.add()}")
