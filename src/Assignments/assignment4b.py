from re import A


attempts = 0


def increaseAttempt():
    global attempts
    attempts = attempts + 1


def addReverse(num: int):
    l = list(str(num))
    l.reverse()
    r = int("".join(l))

    return {"reverse": r, "added": num + r}


def isPalindrome(sum):
    l = list(str(sum))
    l.reverse()
    r = int("".join(l))

    if r == sum:
        return True
    else:
        return False


while True:
    try:
        attempts = 0
        num = int(input("User input: "))

        while True:
            results = addReverse(num)

            print(f"Your number: {results['reverse']}")
            print(f"Added number: {results['added']}")

            res = isPalindrome(results["added"])

            if res == True:
                print(f"Palindrome: ✅")
                increaseAttempt()
                print(f"Attempts: {attempts}")
                break
            else:
                print(f"Palindrome: ❌")
                increaseAttempt()
                print(f"Attempts: {attempts}")
                num = results["added"]
    except Exception as e:
        print(e)
