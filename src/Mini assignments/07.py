import random

def subtotal(number_of_people):
    if number_of_people < 8:
        costPer = random.randint(13, 15)
        return number_of_people * costPer
    else:
        costPer = random.randint(13, 15)
        return (number_of_people * costPer) * 1.15


def tip(subtotal, amount, type):
    if type == "%":
        return subtotal * float(f"0.{amount}")
    if type == "$":
        return int(amount)


def taxes(subtotal):
    return subtotal * 0.15


def final(subtotal, tip, taxes):
    return subtotal + tip + taxes


t = 0


def handle(number_of_people):
    try:
        sub_total = subtotal(number_of_people)

        print(f"Your subtotal is ${sub_total}")

        ti = input(
            "Would you like to tip? If so, enter a percent with a percent sign after the number or enter an amount with a dollar sign in front. If not, just hit enter"
        )

        global t

        if "%" in ti:
            word = list(ti)
            word.remove("%")
            word = "".join(word)
            t = tip(sub_total, word, "%")
        if "$" in ti:
            word = list(ti)
            word.remove("$")
            word = "".join(word)
            t = tip(sub_total, word, "$")
        else:
            t = 0
        print(f"You're paying ${t} in tip")

        tax = taxes(sub_total)

        print(f"The amount of tax is ${tax}")

        total = final(sub_total, t, tax)

        print(f"You're final total is ${total}")

    except Exception as e:
        print(e)


while True:
    people = int(input("How many people are in the party tonight? "))
    handle(people)
