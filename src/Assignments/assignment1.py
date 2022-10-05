while True:
    try:
        num1 = int(input("What is your first number? "))
        num2 = int(input("What is your second number? "))
        operation = input("What is operation would you like to try? ")
        add = lambda a, b: a + b
        subtract = lambda a, b: a - b
        multiply = lambda a, b: a * b
        divide = lambda a, b: a / b
        if operation.lower() == "add":
            print(add(num1, num2))
            continue
        if operation.lower() == "sub":
            print(subtract(num1, num2))
            continue
        if operation.lower() == "multiply":
            print(multiply(num1, num2))
            continue
        if operation.lower() == "divide":
            print(divide(num1, num2))
            continue
        else:
            raise Exception("Invalid Num / Invalid operation")
    except Exception as e:
        print(e)
