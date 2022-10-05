while True:
    try:
        num = int(input("What is your number"))

        def doMath(num):
            print(f"Added your number {num} to 10 which is equal to {num+10}")
            print(f"Multiplied your nunber {num} by 10 which is equal to {num*10}")
            print(f"Divided your number {num} by 10 which is equal to {num/10}")

        doMath(num)
    except Exception as e:
        print(e)
        print("Ayo, why you trying to break the program? ")
        continue