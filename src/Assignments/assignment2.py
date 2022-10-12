import random
import time

def ran(start, end):
    return random.randint(start, end)

def rps(choice):
    bot_choice = ran(1, 3)
    choices = {1: "rock", 2: "paper", 3: "scissors"}
    user_choice = 0
    if choice == "rock":
        user_choice = 1
    if choice == "paper":
        user_choice = 2
    if choice == "scissors":
        user_choice = 3
    print(user_choice == 1)
    if user_choice == 1:
        if bot_choice == 1:
            print("The bot also chose rock!")
            return "retry"
        if bot_choice == 2:
            print("The bot chose rock")
            return "loss"
        if bot_choice == 3:
            print("The bot chose rock")
            return "win"
    if user_choice == 2:
        if bot_choice == 1:
            print("The bot chose paper")
            return "win"
        if bot_choice == 2:
            print("The bot also chose paper")
            return "retry"
        if bot_choice == 3:
            print("The bot chose paper")
            return "loss"
    if user_choice == 3:
        if bot_choice == 1:
            print("The bot chose scissors")
            return "loss"
        if bot_choice == 2:
            print("The bot chose scissors")
            return "win"
        if bot_choice == 3:
            print("The bot chose scissors")
            return "retry"


def dice(guess):
    roll = ran(1, 6)
    print("Rolling...")
    time.sleep(5)
    print(f"The bot rolled {roll}")
    if guess == roll:
        return True
    else:
        return False

def ranNUm(guess):
    rando = ran(1, 50)
    print("Generating...")
    time.sleep(5)
    print(f"The bot got {rando}")
    if guess == rando:
        return True
    else:
        return False

while True:
    game = input("What game would you like to play? (Dice game, rps, guessing) ")

    if game == "rps":
        choice = input("Rock, paper or scissors? ")
        status = rps(choice)
        if status == "win":
            print("Congrats!! You won!")
            continue
        if status == "loss":
            print("L. You lost!")
            continue
        if status == "retry":
            print("Tie!")
            continue
    if game == "dice":
        user_guess = int(input("Pick a number  between 1-6! "))

        result = dice(user_guess)

        if result == True:
            print("Congrats! You won!!")
            continue
        if result == False:
            print("You lost!")
            continue
    if game == "guessing":
        user_guess = int(input("Pick a number between 1-50! "))
        if user_guess > 50 or user_guess < 1:
            print("Number is out of range!")
            continue

        status = ranNUm(user_guess)

        if status == True:
            print("Congrats!!! You won!")
            continue
        if status == False:
            print("L. You lost.")