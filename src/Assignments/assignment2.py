import random
import time

# define a function to generate a random number


def ran(start: int, end: int):
    return random.randint(start, end)


# define a function for the rock paper scissors game


def rps(choice: str):
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
            print("The bot ch2ose rock")
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


# define a function for the dice game


def dice(guess: int):
    # generate a random dice roll

    roll = ran(1, 6)
    print("Rolling...")
    time.sleep(5)

    # tell the user what the bot got

    print(f"The bot rolled {roll}")

    # check if the users guess is the same as the rolled number
    if guess == roll:
        return True
    else:
        return False


# define a function for the random number guessing game


def ranNUm(guess: int):
    # generate a random number

    rando = ran(1, 50)

    print("Generating...")
    time.sleep(5)

    # tell the user, what the bot got

    print(f"The bot got {rando}")

    # check if the provided answer is right

    if guess == rando:
        return True
    else:
        return False


while True:
    # ask the user what game they would like to play

    game = input("What game would you like to play? (Dice, rps, guessing) ")

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
