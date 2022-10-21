import random


def generateList() -> list:
    l = []
    for i in range(3):
        l.append(random.randint(1, 100))
    return l


def findMedian(arr: list) -> str:
    arr.sort()
    return str(arr[1])


while True:
    try:
        t = int(input("1) random number?\n2) entering numbers manually?\n"))

        median = []

        if t == 1:
            median = generateList()
        elif t == 2:
            nums = input("Enter 3 nums seperated by commas").split(",")
            median = nums
        else:
            raise Exception("Invalid Choice!")
        print(f"The original list is: {median}")
        print(f"The median is {findMedian(median)}")
    except Exception as e:
        print(e)
