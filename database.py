class User:
    def __init__(self, name, phone, address, email):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email

    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone

    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email


db = {}

name = input("What is your name? 💳 ")
phone = input("What is your phone number? ☎️ ")
address = input("What is your address? 🏠 ")
email = input("What is your email? 📧 ")

db[name] = User(name, phone, address, email)

print(db)

while True:
    action = int(
        input(
            "What would you like to do next?\n1) Add more infromation to the database?\n2) Search the database\n3) Quit"
        )
    )

    if action == 1:
        name = input("What is your name? 💳 ")
        if name in db:
            print("This name already exists in the database!")
            break
        phone = input("What is your phone number? ☎️ ")
        address = input("What is your address? 🏠 ")
        email = input("What is your email? 📧 ")

        db[name] = User(name, phone, address, email)
    if action == 2:
        query = input("What is the name of the person you would like to search? ")

        if query in db:
            info = db[query]
            print(f"💳 | The name is {info.getName()}")
            print(f"☎️ | The phone number is {info.getPhone()}")
            print(f"🏠 | The address is {info.getAddress()}")
            print(f"📧 | The email is {info.getEmail()}")
    if action == 3:
        print("byee!!! 👋👋👋")
        break
