# part 1


class human:
    def __init__(self, firstname):
        self.firstname = firstname

    def __str__(self) -> str:
        return f"First name: {self.firstname}"


# part 2

num = int(input("How many people are you creating?"))

person_dict = {}

# part 3 for i in range(num):

last = input("Enter SURNAME name")

first = input("Enter FIRST name")

person_dict[last] = human(first)

# part 4 print(person_dict.keys())

ask = input("Which last name would you like to see the first name for?")

print(person_dict[ask])
