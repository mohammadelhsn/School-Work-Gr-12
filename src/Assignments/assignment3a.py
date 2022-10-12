# triangle b * h /2
# rectangle l * w
# parallelogram b * h
# trapezoid a + b /2  * h
# area of circle pi * r^2

# ㎠

import math

triangle = lambda b, h: b * h / 2
rectangle = lambda l, w: l * w
parallelogram = lambda l, w: l * w
trapezoid = lambda a, b, h: (a + b) / 2 * h
circle = lambda r: math.pi * r ^ 2

while True:
    try:
        formula = int(
            input(
                "Which formula would you like to use?\n1) Triangle\n2) Rectangle\n3) Parallelogram\n4) Trapezoid\n5) Circle\n6) Quit\n"
            )
        )

        if formula == 1:
            base = int(input("What is the base of the triangle? "))
            height = int(input("What is the height of the triangle? "))
            area = triangle(base, height)
            print(
                f"The area of the triangle with a base of {base}cm and a height of {height}cm is {area}㎠"
            )
            continue
        if formula == 2:
            length = int(input("What is the length of the rectangle (in cm)? "))
            width = int(input("What is the height of the rectanlge (in cm)? "))
            area = rectangle(length, width)
            print(
                f"The area of a rectangle with a length of {length}cm and a width of {width}cm is {area}㎠"
            )
            continue
        if formula == 3:
            base = int(input("What is the base of the parallelogram? "))
            height = int(input("What is the height of the parallelogram? "))
            area = parallelogram(base, height)
            print(
                f"The area of the parallelogram with a base of {base}cm and a height of {height}cm is {area}㎠"
            )
            continue
        if formula == 4:
            a = int(input("What is the a value of your trapezoid? "))
            b = int(input("What is the b value of your trapezoid? "))
            height = int(input("What is the height of your trapezoid? "))
            area = trapezoid(a, b, height)
            print(
                f"The area of a trapezoid with an a value of {a}cm and a b value of {b}cm and a height of {height}cm is {area}㎠"
            )
            continue
        if formula == 5:
            radius = int(input("What is the radius of the circle? "))
            area = circle(radius)
            print(f"The area of a circle with a radius of {radius} is {area}㎠")
        if formula == 6:
            break
        else:
            print("Hey! You can't do that!")
            continue
    except Exception as e:
        print(e)
        continue
