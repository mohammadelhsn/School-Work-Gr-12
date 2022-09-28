import random

words = [
    {
        "english": "hello",
        "translation": "bonjour",
        "points": random.randrange(50, 300, 50),
        "hints": [],
    },
    {
        "english": "yes",
        "translation": "oui",
        "points": random.randrange(50, 300, 50),
        "hints": [],
    },
    {
        "english": "no",
        "translation": "non",
        "points": random.randrange(50, 300, 50),
        "hints": [],
    },
    {
        "english": "thanks",
        "translation": "merci",
        "points": random.randrange(50, 300, 50),
        "hints": [],
    },
    {
        "english": "man",
        "translation": "homme",
        "points": random.randrange(50, 300, 50),
        "hints": [],
    },
    {
        "english": "woman",
        "translation": "femme",
        "points": random.randrange(50, 300, 50),
        "hints": [],
    },
    {
        "english": "time",
        "translation": "temps",
        "points": random.randrange(50, 300, 50),
        "hints": [],
    },
    {
        "english": "cat",
        "translation": "chat",
        "points": random.randrange(50, 300, 50),
        "hints": [],
    },
    {
        "english": "day",
        "translation": "jour",
        "points": random.randrange(50, 300, 50),
        "hints": [],
    },
    {
        "english": "world",
        "translation": "monde",
        "points": random.randrange(50, 300, 50),
        "hints": [],
    },
]
guesses = 3
attempts = int(input("How many words would you like to attempt? "))
toguess = []
points = 0
correct = 0
incorrect = 0

for i in range(attempts):
    choice = random.choice(words)
    toguess.append(choice)
    words.remove(choice)

for word in toguess:
    word_len = len(word["english"])
    translation = word["translation"]
    print(f"The length of the word is {word_len}")
    print(f"The french word is {translation}")
    print(f"You have {points} point(s)")

    for i in range(3):
        guess = input("What is your guess for the word? ")
        english = word["english"]
        if guesses > 0:
            if guess.lower() == english:
                points = points + word["points"]
                print("✅ | You guessed correct! Niceeee! ")
                correct += 1
                break
            else:
                print("❌ | You guessed wrong!")
                guesses -= 1
                points = points - random.randint(50, 100)
        else:
            print("❌ | You ran out of guesses!")
            print(f"The word was {english}")
            incorrect += 1
            break

print(f"You finished this game with {points}")
