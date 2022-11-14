#############################################################################
#Author: Mohammad El-Hassan
#Description: Mini Assingment #64
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

import time

userinfo = {}
phone = input("What is your phone number ")
userinfo["phone"] = phone
cellphone = input("What is your cellphone number? ")
userinfo["cellphone"] = cellphone
fax = input("What is your fax number? ")
userinfo["fax"] = fax
print(userinfo)
time.sleep(5)
print("What are you a doctor or something??? We don't use faxes anymore LOL ")
del userinfo["fax"]
print(userinfo)
