import random
import time
import string

letters = list(string.ascii_letters)
nums = list(range(1, 10))


def generatePass():
    length = random.randint(1, 8)
    nu = random.randint(1, 2)

    password = ""

    for i in range(nu):
        choice = random.choice(nums)
        password = password + f"{choice}"

    for i in range(length - 2):
        choice = random.choice(letters)
        password = password + choice

    return password


def countCheck(string: str):
    if len(string) < 8:
        return False
    else:
        return True


def numCheck(string: str):
    nums = 0
    for char in string:
        if char.isdigit():
            nums += 1
        else:
            continue

    if nums < 2:
        return False
    else:
        return True


def lowerCheck(string: str):
    count = 0
    for char in string:
        if char.islower():
            count += 1
        else:
            continue

    if count < 1:
        return False
    else:
        return True


def upperCheck(string: str):
    count = 0
    for char in string:
        if char.isupper():
            count += 1
        else:
            continue

    if count < 1:
        return False
    else:
        return True


attempts = 0

while True:
    try:
        password = generatePass()

        print("Generating password!")

        time.sleep(2)

        print(f"The password is {password}")

        countRes = countCheck(password)

        if countRes == True:
            time.sleep(2)
            print("✅ | Passed!")
        if countRes == False:
            time.sleep(2)
            print("❌ | The password entered doesn't meet the minimum character length")
            attempts = attempts + 1
            continue

        numberCheck = numCheck(password)
        if numberCheck == True:
            time.sleep(2)
            print("✅ | Passed!")
        if numberCheck == False:
            time.sleep(2)
            print("❌ | The password doesn't have the minimum required numbers")
            attempts = attempts + 1
            continue

        lowCheck = lowerCheck(password)
        if lowCheck == True:
            time.sleep(2)
            print("✅ | Passed!")
        if lowCheck == False:
            time.sleep(2)
            print("❌ | The password doesn't meet the minimum lower char requirements")
            attempts = attempts + 1
            continue

        upCheck = upperCheck(password)

        if upCheck == True:
            time.sleep(2)
            print("✅ | Passed!")
            attempts += 1
            print(f"Game over! Took the program {attempts} attempt(s) to get it!")
            break
        if upCheck == False:
            time.sleep(2)
            print(
                "❌ | The password doesn't meet the minimum requirements for uppercase letters"
            )
            attempts = attempts + 1
            continue

    except Exception as e:
        print(e)
