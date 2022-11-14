#############################################################################
#Author: Mohammad El-Hassan
#Description: Mini Assingment #67
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

dict_1 = {0: 34, 1: 500, 2: 642, 3: 2, 4: 67, 5: 8000, 6: 234}
lowest = 0
for i in range(len(dict_1)):
    num = dict_1[i]
    if lowest == 0:
        lowest = num
    if num < lowest:
        lowest = num
    continue
print(f"THe lowest numnber is {lowest}")
