#############################################################################
#Author: Mohammad El-Hassan
#Description: Mini Assingment #61
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

gamers = [
    "plasma rifle",
    "assault rifle",
    "ammo",
    "machette",
    " hand gun",
    "HUD helmet",
]
index_of_ammo = gamers.index("ammo")
gamers.insert(index_of_ammo, "body armour")
print(gamers)
