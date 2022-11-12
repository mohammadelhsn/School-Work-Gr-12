#############################################################################
#Author: Mohammad El-Hassan
#Description: Assignemnt #3c
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

import time


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


while True:
    try:
        password = input("What is your password ")

        countRes = countCheck(password)

        if countRes == True:
            time.sleep(2)
            print("✅ | Passed!")
        if countRes == False:
            print("❌ | The password entered doesn't meet the minimum character length")
            continue

        numberCheck = numCheck(password)
        if numberCheck == True:
            time.sleep(2)
            print("✅ | Passed!")
        if numberCheck == False:
            print("❌ | The password doesn't have the minimum required numbers")
            continue

        lowCheck = lowerCheck(password)
        if lowCheck == True:
            time.sleep(2)
            print("✅ | Passed!")
        if lowCheck == False:
            print("❌ | The password doesn't meet the minimum lower char requirements")
            continue

        upCheck = upperCheck(password)

        if upCheck == True:
            time.sleep(2)
            print("✅ | Passed!")
        if upCheck == False:
            print(
                "❌ | The password doesn't meet the minimum requirements for uppercase letters"
            )
            continue

    except Exception as e:
        print(e)
