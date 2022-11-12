#############################################################################
#Author: Mohammad El-Hassan
#Description: Mini Assingment #68
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

d = {"1": "1", "2": "2", "3": "3", "4": "4"}
while True:
    selection = int(
        input(
            "What would you like to do? \n1. Update/Add to the dictionary\n2. Delete from the dictionary\n3. Clear the dictionary list\n4. Quit\n"
        )
    )
    if selection == 1:
        print("You have chosen to update/add")
        choice = int(input("Would you like to (1) Update or (2) add something? "))
        if choice == 1:
            toUpdate = input("What key would you like to update? ")
            if toUpdate in d.keys():
                newValue = input("What is the new value? ")
                d[toUpdate] = newValue
                print(f"Successfully updated {toUpdate} to {newValue}")
                print(d)
            else:
                print("This key doesn't exist in the dictionary")
                continue
        if choice == 2:
            toUpdate = input("What would you like the key to be? ")
            if toUpdate not in d.keys():
                value = input("What would you like the value to be? ")
                d[toUpdate] = value
                print(f"The new key, {toUpdate} has now been set to {value}")
                print(d)
            else:
                print("This key already exists!! Try updating instead!")
                continue
        else:
            print("Invalid selection!")
            continue
    if selection == 2:
        print(d)
        if len(d) == 0:
            print(
                "You cannot delete anything from an empty dictionary. Try inserting something first."
            )
            continue
        print("You have chosen to delete from the dictionary")
        toDelete = input("What would you like to delete? ")
        if d.get(toDelete) == None:
            continue
        del d[toDelete]
        print(f"{toDelete} has been deleted from the dictionary")
        print(d)
    if selection == 3:
        print("You have chosen to clear the dictionary")
        d.clear()
        print(d)
    if selection == 4:
        print("You have chosen to quit the program")
        print(d)
        break
    else:
        continue
