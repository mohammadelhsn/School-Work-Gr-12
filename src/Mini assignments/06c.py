while True:
    try:
        phrase = input("What phrase would you like to center?")
        if phrase == "quit":
            break
        width = int(input("What is the width of your page? "))
        length = len(phrase)
        print(f"The length of your phrase is {length}")
        space = (width - length) / 2
        print(f"The space on either side of your prhase is {space}")
        print(f"_" * round(space) + f"{phrase}" + f"_" * round(space))
    except Exception as e:
        print(e)
