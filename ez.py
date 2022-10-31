hp = 5
rand = 6


def fight(armour, hit, hp):
    print(f"You have been attacked and dealt for {hit} points")

    if armour < 3:
        print("you have blocked the blow")
        hp = hp - (hit - 2)
    else:
        print("You have been hit")
        hp = hp - hit
    if hp <= 0:
        print("you have died")
    else:
        print(f"You have {hp} hp left")


fight(2, rand, hp)
