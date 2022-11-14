#############################################################################
#Author: Mohammad El-Hassan
#Description: Mini Assingment #12
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

import collections
import time

while True:
    try:
        nums = int(input("How many numbers would you like the list to be? "))

        arr = []
        array = collections.deque([])

        for i in range(nums):
            item = input("What item would you like to append? ")
            arr.append(item)

        print(f"This is list 1: {arr}")
        print(f"This is list 2: {array}")

        for i in range(len(arr)):
            print(f"This is the length of the list: {len(arr)}")
            print(f"This is the length of the array: {len(array)}")
            time.sleep(1)
            popped = arr.pop()
            array.append(popped)

            print(f"This the decreasing first list: {arr}")
            print(f"This is the increasing second array: {array}")
            time.sleep(1)

        for i in range(len(array)):
            print(f"This is the length of the list: {len(arr)}")
            print(f"This is the length of the array: {len(array)}")
            time.sleep(1)

            popped = array.pop()
            arr.append(popped)

            print(f"This the increasing first list: {arr}")
            print(f"This is the decreasing second array: {array}")
            time.sleep(1)

    except Exception as e:
        print(e)
