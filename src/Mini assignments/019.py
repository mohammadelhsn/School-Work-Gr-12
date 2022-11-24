#############################################################################
# Author: Mohammad El-Hassan
# Description: Mini-assignment #19
# Date Created: 11/19/2022
# Date Modified: 11/19/2022
#############################################################################


class Bank:
    def __init__(self, name, bal=0.0):
        self.standard = Standard(name, bal)
        self.joint = Joint(name)


class Standard:
    joint = 0

    def __init__(self, name, balance=0.0):
        self.bal = balance
        self.name = name

    def viewbal(self):
        return print(f"🏦 | {self.name}'s standard account balance is ${self.bal}")

    def isZero(self, toWithdraw):
        if (self.bal - toWithdraw) < 0:
            print("❌ | You can't withdraw that amount")
            return True
        if self.bal - toWithdraw == 0:
            print("❌ | You have no money in the account!")
            return False
        else:
            False

    def deposit(self, amt: float):
        self.bal = self.bal + amt

        print(
            f"✅ | Successfully deposited ${amt} into {self.name}'s standard bank account!"
        )
        self.viewbal()
        return

    def withdraw(self, amt: float):
        res = self.isZero(amt)
        if amt == 0.0:
            print("❌ | You can't withdraw 0!")
            return self
        if res == True:
            return self
        else:
            self.bal = self.bal - amt

            print(
                f"✅ | Successfully withdrew ${amt} into {self.name}'s standard bank account!"
            )
            self.viewbal()
            return


class Joint:
    bal = 0.0
    owners = []

    def __init__(self, name) -> None:
        Joint.owners.append(name)
        self.accessor = name
        pass

    def isZero(self, toWithdraw):
        if (Joint.bal - toWithdraw) < 0:
            print("❌ | You can't withdraw that amount")
            return True
        if Joint.bal - toWithdraw == 0:
            print("❌ | You have no money in the account!")
            return False
        else:
            False

    def viewbal(self):
        return print(
            f"🏦 | The bank account owned by: {', '.join(Joint.owners)}'s balance is ${Joint.bal}"
        )

    def deposit(self, amt: float):
        Joint.bal = Joint.bal + amt

        print(
            f"✅ | {self.accessor} successfully deposited ${amt} into the joint account"
        )

        self.viewbal()
        return

    def withdraw(self, amt: float):
        res = self.isZero(amt)
        if amt == 0.0:
            print("❌ | You can't withdraw 0!")
            return self
        if res == True:
            return self
        else:
            Joint.bal = Joint.bal - amt

            print(
                f"✅ | {self.accessor} successfully withdrew ${amt} from the joint account"
            )

            return self.viewbal()


user1 = Bank("User 1")
user2 = Bank("User 2")

users = [user1, user2, user1.joint, user2.joint]

while True:
    try:
        account = int(
            input(
                "❓ | Which account are you using?\n1) User 1 (Standard 🧑)\n2) User 2 (Standard 🧑)\n3) User 1 (Joint 🧑‍🤝‍🧑)\n4) User 2 (Joint 🧑‍🤝‍🧑)\n"
            )
        )
        action = int(
            input(
                "❓ | What action would you like to perform on the account?\n1) View Balance\n2) Deposit\n3) Withdraw\n"
            )
        )

        account = users[account - 1]

        if action == 1:
            account.viewbal()
        if action == 2:
            amt = float(input("❓ | How much would you like to deposit? "))

            if amt == 0.0:
                print("❌ | That is an invalid amount!")
                continue
            else:
                account.deposit(amt)
        if action == 3:
            amt = float(input("❓ | How much would you like to withdraw? "))

            if amt == 0.0:
                print("❌ | That is an invalid amount!")
                continue
            else:
                account.withdraw(amt)
    except Exception as e:
        print(e)
        continue
