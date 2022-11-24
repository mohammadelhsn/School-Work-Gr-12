class Bank:
    holders = []
    joint_bal = 0.0

    def __init__(self, name, bal=0.0):
        self.name = name
        self.accessor = self.name
        Bank.holders.append(name)
        self.bal = bal

    def isZeros(self, toWithdraw):
        if (self.bal - toWithdraw) < 0:
            print("❌ | You can't withdraw that amount")
            return True
        if self.bal - toWithdraw == 0:
            print("❌ | You have no money in the account!")
            return False
        else:
            False

    def isZeroj(self, toWithdraw):
        if (Bank.joint_bal - toWithdraw) < 0:
            print("❌ | You can't withdraw that amount")
            return True
        if Bank.joint_bal - toWithdraw == 0:
            print("❌ | You have no money in the account!")
            return False
        else:
            False

    def viewbals(self):
        return print(f"🏦 | {self.name}'s standard account balance is ${self.bal}")

    def viewbalj(self):
        return print(
            f"🏦 | The bank account owned by: {', '.join(Bank.holders)}'s balance is ${Bank.joint_bal}"
        )

    def deposits(self, amt: float):
        self.bal = self.bal + amt

        print(
            f"✅ | Successfully deposited ${amt} into {self.name}'s standard bank account!"
        )
        self.viewbals()
        return

    def deopsitj(self, amt: float):
        Bank.joint_bal = Bank.joint_bal + amt

        print(
            f"✅ | {self.accessor} successfully deposited ${amt} into the joint account"
        )

        self.viewbalj()
        return

    def withdraws(self, amt: float):
        res = self.isZeros(amt)
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
            self.viewbals()
            return

    def withdrawj(self, amt: float):
        res = self.isZeroj(amt)
        if amt == 0.0:
            print("❌ | You can't withdraw 0!")
            return self
        if res == True:
            return self
        else:
            Bank.joint_bal = Bank.joint_bal - amt

            print(
                f"✅ | {self.accessor} successfully withdrew ${amt} from the joint account"
            )

            return self.viewbalj()


user1 = Bank("User 1")
user2 = Bank("User 2")

while True:
    try:
        account = int(
            input(
                "❓ | Which account are you using?\n1) User 1 (Standard 🧑)\n2) User 1 (Joint 🧑‍🤝‍🧑)\n3) User 2 (Standard 🧑)\n4) User 2 (Joint 🧑‍🤝‍🧑)\n"
            )
        )

        action = int(
            input(
                "❓ | What action would you like to perform on the account?\n1) View Balance\n2) Deposit\n3) Withdraw\n"
            )
        )

        if account == 1 and action == 1:
            user1.viewbals()
        if account == 1 and action == 2:
            amt = float(input("❓ | How much would you like to deposit? "))

            if amt == 0.0:
                print("❌ | That is an invalid amount!")
                continue
            else:
                user1.deposits(amt)
        if account == 1 and action == 3:
            amt = float(input("❓ | How much would you like to withdraw? "))

            if amt == 0.0:
                print("❌ | That is an invalid amount!")
                continue
            else:
                user1.withdraws(amt)

        # Joint account methods

        if account == 2 and action == 1:
            user1.viewbalj()
        if account == 2 and action == 2:
            amt = float(input("❓ | How much would you like to deposit? "))

            if amt == 0.0:
                print("❌ | That is an invalid amount!")
                continue
            else:
                user1.deopsitj(amt)
        if account == 2 and action == 3:
            amt = float(input("❓ | How much would you like to withdraw? "))

            if amt == 0.0:
                print("❌ | That is an invalid amount!")
                continue
            else:
                user1.withdrawj(amt)

            # Account 2

        if account == 3 and action == 1:
            user2.viewbals()
        if account == 3 and action == 2:
            amt = float(input("❓ | How much would you like to deposit? "))

            if amt == 0.0:
                print("❌ | That is an invalid amount!")
                continue
            else:
                user2.deposits(amt)
        if account == 3 and action == 3:
            amt = float(input("❓ | How much would you like to withdraw? "))

            if amt == 0.0:
                print("❌ | That is an invalid amount!")
                continue
            else:
                user2.withdraws(amt)

        # Joint account methods

        if account == 4 and action == 1:
            user2.viewbalj()
        if account == 4 and action == 2:
            amt = float(input("❓ | How much would you like to deposit? "))

            if amt == 0.0:
                print("❌ | That is an invalid amount!")
                continue
            else:
                user2.deopsitj(amt)
        if account == 4 and action == 3:
            amt = float(input("❓ | How much would you like to withdraw? "))

            if amt == 0.0:
                print("❌ | That is an invalid amount!")
                continue
            else:
                user2.withdrawj(amt)
    except Exception as e:
        print(e)
        continue
