""""
call on a random number generator method that will determine a random number between 1-10 (do this once for each enemy).  If the random number is greater than 7,  - output the random number and the enemy it is associated with - then you must set the enemies "life" to a ZERO and print ("critical"). 

If the random number is between 1-6 - output the random number and the enemy it is associated with - and then run the attack method only.

each enemy will get one attack

each enemy will check to see if they are still alive 
"""
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
