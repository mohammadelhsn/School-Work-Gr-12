# mini assignment 17

import random


def main():
    # create a list of 10 random numbers
    numbers = []
    for i in range(10):
        numbers.append(random.randint(1, 100))

    # print the list
    print(numbers)

    # print the average of the list
    print("The average is", sum(numbers) / len(numbers))

    # print the highest number in the list
    print("The highest number is", max(numbers))

    # print the lowest number in the list
    print("The lowest number is", min(numbers))

    # print the sum of the list
    print("The sum is", sum(numbers))

    # print the numbers in the list that are greater than the average
    print("The numbers greater than the average are", end=" ")
    for i in numbers:
        if i > sum(numbers) / len(numbers):
            print(i, end=" ")


main()
