import math

# define lambda functions to calculate the area

triangle = lambda b, h: b * h / 2
rectangle = lambda l, w: l * w
parallelogram = lambda l, w: l * w
trapezoid = lambda a, b, h: (a + b) / 2 * h
circle = lambda r: math.pi * r ^ 2

while True:
    try:
        # ask the user which formula they need

        formula = int(
            input(
                "Which formula would you like to use?\n1) Triangle\n2) Rectangle\n3) Parallelogram\n4) Trapezoid\n5) Circle\n6) Quit\n"
            )
        )

        # if the formula chosen is 1

        if formula == 1:
            # ask the user for the input

            base = int(input("What is the base of the triangle? "))
            height = int(input("What is the height of the triangle? "))

            # call the lambda function

            area = triangle(base, height)

            # Output the result and restart the loop again.

            print(
                f"The area of the triangle with a base of {base}cm and a height of {height}cm is {area}㎠"
            )
            continue
        if formula == 2:
            # ask the user for the input

            length = int(input("What is the length of the rectangle (in cm)? "))
            width = int(input("What is the height of the rectanlge (in cm)? "))

            # call the lambda function

            area = rectangle(length, width)

            # output the result and begin the loop again.

            print(
                f"The area of a rectangle with a length of {length}cm and a width of {width}cm is {area}㎠"
            )
            continue
        if formula == 3:
            # ask the user for the input

            base = int(input("What is the base of the parallelogram? "))
            height = int(input("What is the height of the parallelogram? "))

            # call the lambda function
            area = parallelogram(base, height)

            # output the result and restart the loop

            print(
                f"The area of the parallelogram with a base of {base}cm and a height of {height}cm is {area}㎠"
            )
            continue
        if formula == 4:

            # ask the user for the input

            a = int(input("What is the a value of your trapezoid? "))
            b = int(input("What is the b value of your trapezoid? "))
            height = int(input("What is the height of your trapezoid? "))

            # call the lambda function

            area = trapezoid(a, b, height)

            # output the result and restart the loop

            print(
                f"The area of a trapezoid with an a value of {a}cm and a b value of {b}cm and a height of {height}cm is {area}㎠"
            )
            continue
        if formula == 5:
            # ask the user for the input

            radius = int(input("What is the radius of the circle? "))

            # call the lambda function
            area = circle(radius)

            # output the result and restart the loop

            print(f"The area of a circle with a radius of {radius} is {area}㎠")
        if formula == 6:
            # they're trying to quit the program
            break
        else:
            # invalid choice
            print("Hey! You can't do that!")
            continue
    except Exception as e:
        print(e)
        continue
