attempts = 0


def increaseAttempt():
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
        num = int(input("User input: "))
        results = addReverse(num)

        print(f"Your number: {results['reverse']}")
        print(f"Added number: {results['added']}")

        res = isPalindrome(results["added"])

        if res == True:
            print(f"Palindrome: ✅")
            increaseAttempt()
            print(f"Attempts: {attempts}")
        else:
            print(f"Palindrome: ❌")
            increaseAttempt()
            print(f"Attempts: {attempts}")
    except Exception as e:
        print(e)
