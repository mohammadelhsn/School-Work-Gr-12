def displayTotal(i=0, total=0):
    try:
        m = int(input("Enter a number of hit enter"))

        total += m
        print(total)
        displayTotal(m, total)

    except Exception as e:
        print(total)
        displayTotal(i, total)


while True:
    displayTotal()
