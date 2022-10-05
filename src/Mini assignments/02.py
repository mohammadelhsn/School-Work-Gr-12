import random

while True:
    try:
        start = int(input("Where would you like the range to start from? "))
        end = int(input("Where would you like the range to end? "))

        if end < start:
            raise Exception("The end lower is higher than the beginning number")

        def generator(start, end):
            return random.randrange(start, end, 2)

        print(generator(start, end))

    except Exception as e:
        print(e)
        continue
