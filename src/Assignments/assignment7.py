import random


class Songs:
    def __init__(self):
        pass

    def line1(self):
        print("row, row, row your boat")

    def line2(self):
        print("Gently down the stream")

    def line3(self):
        print("Merrily, merrily, merrily, merrily")

    def line4(self):
        print("Life is but a dream")

    def line5(self):
        print("Never gonna give you up")

    def line6(self):
        print("Hey now, you're a rockstar")


try:
    songs = Songs()

    funcs = [
        songs.line1,
        songs.line2,
        songs.line3,
        songs.line4,
        songs.line5,
        songs.line6,
    ]

    random.shuffle(funcs)
    for func in funcs:
        func()

except Exception as e:
    print(e)
