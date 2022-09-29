import random
import time

amount = 100

while True:
    if amount == 0:
        print("You're out of money! Game over!")
        break
    user_bet = 0
    while user_bet < 100:
        user_bet = int(input("How much money would you like to bet? "))
    bot_bet = user_bet
    print("Look at that! The program is also betting the same amount! ")

    user_num = 0
    while user_num > 6 or user_num < 1:
        user_num = int(input("What number would you like to bet on (1-6)? "))
    nums = [1, 2, 3, 4, 5, 6]
    nums.remove(user_num)
    choice = random.choice(nums)
    dice_roll = random.randint(1, 6)

    print(f"The bot guessed {choice}")

    print("Rolling...")
    time.sleep(5)
    print(f"The dice rolled {dice_roll}")

    if dice_roll == user_num:
        amount = amount + user_bet + bot_bet
        print(f"Nice job! You win! Your amount is ${amount}")
        continue
    if dice_roll == choice:
        amount = amount - user_bet / 2
        print(f"❌ | The bot guessed it correct! Your amount is now ${amount}")
        continue
    else:
        amount = amount - user_bet / 4
        print(f"❌ | Both you and the bot guessed it wrong! ${amount}")
        continue
