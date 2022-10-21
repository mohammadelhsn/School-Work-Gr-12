class ez:
    def __init__(self, string) -> None:
        self.string = string
        pass

    def Capitalize(self, *args: str):
        if (args): 
            print(args)


a = ez("hello there")
a.Capitalize()
