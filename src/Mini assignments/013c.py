def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)


try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("The GCF of", a, "and", b, "is", gcf(a, b))
except Exception as e:
    print(e)
