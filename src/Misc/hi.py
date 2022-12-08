class Student:
    name = "unknown"  # class attribute

    def __init__(self):
        self.age = 20  # instance attribute

    @staticmethod
    def tostring():
        print("Student Class")

    @classmethod
    def tostring2(cls):
        print("Student Class Attributes: name=", cls.name, ", age=", cls.age)


student = Student().tostring()
Student.tostring2()
