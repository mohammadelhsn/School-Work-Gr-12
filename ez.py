class Person:
    def __new__(cls, first_name, last_name):
        obj = super().__new__(cls)

        obj.first_name = first_name
        obj.last_name = last_name
        obj.full_name = f"{first_name} {last_name}"
        obj.hi = cls.hi
        return obj
    def hi(): return "hi"
student1 = Person("John", "Doe")
print(student1.__dict__)
