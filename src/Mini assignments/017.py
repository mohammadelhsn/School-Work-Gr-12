#############################################################################
# Author: Mohammad El-Hassan
# Description: Mini Assingment #17
# Date Created: 11/16/2022
# Date Modified: 11/16/2022
#############################################################################


class Enemy:
    def __init__(self, colour: str, hp: int, armour: int, weapon: str):
        self.colour = colour
        self.hp = hp
        self.armour = armour
        self.weapon = weapon

    def seeColour(self):
        print(self.colour)

    def seeHp(self):
        print(self.hp)

    def seeArmour(self):
        print(self.armour)

    def seeWeapon(self):
        print(self.weapon)


while True:
    try:
        colour = input("What colour would you like the enemy to be? ")
        hp = int(input("What would you like the HP to be for the enemy? "))
        armour = int(input("How much armour would you like the enemy to have? "))
        weapon = input("What weapon would you like the user to use? ")

        enemy = Enemy(colour, hp, armour, weapon)

        while True:
            property = int(
                input(
                    "What property would you like to see?\n1) Colour\n2) HP\n3) Armour\n4) Weapon\n5) Quit"
                )
            )

            if property == 1:
                enemy.seeColour()
            if property == 2:
                enemy.seeHp()
            if property == 3:
                enemy.seeArmour()
            if property == 4:
                enemy.seeWeapon()
            if property == 5:
                break
        break
    except Exception as e:
        print(e)
