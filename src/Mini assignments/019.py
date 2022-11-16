""""
1) Create a bank account that let's the user have both withdrawals and deposits.  
Each person should be their own object so that each deposit and withdrawal should only affect the individual 
bank accounts, not each other.  Make a attribute inside of the __init__ to set the balance to zero (default). 
If during withdrawal, they reach "0", use a conditional to let them know they have no money in the account.

2) Create another bank account where it is a joint account and anyone can withdraw or deposit to the amount. 
If they reach "0", use a conditional to let them know they have no money in the account.
"""


class Standard:
    def __init__(self, balance=0.0):
        self.bal = balance

    def isZero(self, toWithdraw):
        if (self.bal - toWithdraw) < 0:
            print("You can't withdraw that amount")
            return True
        if self.bal - toWithdraw == 0:
            print("You have no money in the account!")
            return False
        else:
            False

    def deposit(self, amt: float):
        self.bal = self.bal + amt

    def withdraw(self, amt: float):
        res = self.isZero(amt)
        if amt == 0.0:
            print("You can't withdraw 0!")
            return self
        if res == True:
            return self
        else:
            self.bal = self.bal - amt


class Joint:
    bal = 0.0

    def __init__(self) -> None:
        pass

    def isZero(self, toWithdraw):
        if (self.bal - toWithdraw) < 0:
            print("You can't withdraw that amount")
            return True
        if self.bal - toWithdraw == 0:
            print("You have no money in the account!")
            return False
        else:
            False

    def deposit(self, amt: float):
        self.bal = self.bal + amt

    def withdraw(self, amt: float):
        res = self.isZero(amt)
        if amt == 0.0:
            print("You can't withdraw 0!")
            return self
        if res == True:
            return self
        else:
            self.bal = self.bal - amt


user1 = Standard()
user2 = Standard()

user1_joint = Joint()
user2_joint = Joint()

while True:
    try:
        print("hi")
    except Exception as e:
        print(e)
