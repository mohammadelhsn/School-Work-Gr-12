while True:
    print("Please enter all of the following numbers")

    # Get all the values

    a = int(input("What is side a? "))
    b = int(input("What is side b? "))
    c = int(input("What is side c? "))

    # Calculate the C value

    calculated = (a**2) + (b**2)

    # if the c value is equal to the calculate value

    if calculated == c:
        print("This triangle is a right triangle")
    else:
        print("This triangle is not a right triangle")
