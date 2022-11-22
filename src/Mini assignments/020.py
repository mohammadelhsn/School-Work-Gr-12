#############################################################################
# Author: Mohammad El-Hassan
# Description: Mini-assignment #20
# Date Created: 11/19/2022
# Date Modified: 11/19/2022
#############################################################################


class Assignment:
    def __init__(self, lines) -> None:
        self.lines = lines
        pass

    def __str__(self) -> str:
        return "\n".join(self.lines)


while True:
    try:
        lines = []
        for i in range(4):
            line = input("Enter a line from a song: ")
            lines.append(line)

        a = Assignment(lines)
        print(a)
    except Exception as e:
        print(e)
