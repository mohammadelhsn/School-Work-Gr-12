def printTriangle(rows: int):
    if rows == 0:
        return

    print("*" * rows)
    printTriangle(rows - 1)


while True:
    try:
        rows = int(input("How many rows? "))

        printTriangle(rows)
    except Exception as e:
        print(e)
