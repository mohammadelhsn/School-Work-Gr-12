def factorial(num: int):
    print(num)
    if num <= 1:
        return num
    else:
        return num * factorial(num - 1)


print(factorial(5))
