total = 0


def add(l: list):
    a = l.pop()
    print(l)
    add(l)


add([1, 2, 3])
