#############################################################################
#Author: Mohammad El-Hassan
#Description: Mini-assignment #18
#Date Created: 11/22/2022
#Date Modified: 11/22/2022
#############################################################################

import random


class Badguy:
    def __init__(self, name):

        self.hp = 4
        self.name = name
        self.random = 0

    def ranNum(self):
        self.random = random.randint(1,10)

        print(f"The random number for {self.name} is {self.random}")

    def attack(self):

        self.ranNum()

        if (self.random >= 7): 
            print("critical")
            self.hp = 0
        else: 
            print("hit")
            self.hp -= 1

    def still_alive(self):

        if self.hp <= 0:

            print("enemy destroyed")

        else:

            print(str(self.hp) + " hp left")


enemy1 = Badguy("enemy1")

enemy2 = Badguy("enemy2")

enemy1.attack()

enemy2.attack()

enemy1.still_alive()

enemy2.still_alive()
