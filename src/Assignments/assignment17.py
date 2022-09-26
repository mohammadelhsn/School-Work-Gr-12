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

guesses = 3  # per question
attempts = int(input("How many words would you like to attempt? "))
toguess = []

for i in range(attempts):
    choice = random.choice(words)
    toguess.append(choice)
    words.remove(choice)

print(toguess)

for word in toguess:
    word_len = len(word["translation"])
    print(f"The length of the word is {word_len}")
