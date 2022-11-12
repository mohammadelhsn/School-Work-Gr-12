#############################################################################
#Author: Mohammad El-Hassan
#Description: Assignemnt #6b
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

import collections
import random

def generateList():
    nums = collections.deque([]) 
    for i in range(20):
        nums.append(random.randint(1,99))
    return nums

def iterate(total: int, arr: collections.deque):
    if (len(arr) == 1): return False 


    added = arr[0] + arr[1]

    print(f'{arr[0]} + {arr[1]} = {total}? {arr[0] + arr[1] == total}')

    if (total == added): 
        return True
    else: 
        arr.popleft()
        return iterate(total, arr)

while True: 
    try: 
        arr = generateList()

        print(f"The randomly selected nums: {arr}")

        num = int(input("What number would you like it to sum to? "))

        res = iterate(num, arr)

        if (res == True): print("There was a match!")
        else: print(f"None of the numbers added to {num}")


    except Exception as e: 
        print(e)