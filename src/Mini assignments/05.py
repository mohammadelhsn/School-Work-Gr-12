#############################################################################
#Author: Mohammad El-Hassan
#Description: Mini Assingment #5
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

def getWord(lang):
    if lang == "en":
        return "Hello!"
    if lang == "fr":
        return "Salut!"
    if lang == "es":
        return "Hola!"
    else:
        return "error"


while True:
    try:
        lang = input(
            "What language would you like to translate 'hello' to?\n1) English (en)\n2) French (fr)\n3) Spanish (es)\n4) Quit\n "
        )

        if lang == "quit":
            break
        word = getWord(lang)
        if word == "error":
            print("Not a valid choice! 🤨🤨")
            continue
        print(f"Hello in {lang} is {word}")
    except Exception as e:
        print("Why you tryna break the program? 🤨🤨🤨")
        print(e)
        continue
