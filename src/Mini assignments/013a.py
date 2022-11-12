#############################################################################
#Author: Mohammad El-Hassan
#Description: Mini Assingment #13a
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

def sum(arr: list, index=0, total=0):
    # if the index is higher than the length of the array - 1 (so if the index is higher than the last item in the array)

    if (index > len(arr) - 1):
        return total
    else:         
        total = total + arr[index]
        index = index + 1
        return sum(arr, index, total)

while True:
    try:
        # Get user input

        num = input("What is the number? ")

        # Since the input is a string, we're going to split the string and append it to a new list, and while we do that make everything a integer so we can use it in the functin

        nums = []
        i: str
        for i in  num:
            nums.append(int(i))

        # Call the function, print the result to the console. 

        print(f"The sum of the numbers is {sum(nums)}")
    except Exception as e:
        # Print error to the console for debugging.  

        print(e)
