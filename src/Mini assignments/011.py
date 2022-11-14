#############################################################################
#Author: Mohammad El-Hassan
#Description: Mini Assingment #11
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

def appendCourses(arr: list):
    arr.append("advanced functions")
    arr.append("computer science")
    arr.append("physics")
    arr.append("englsih")
    arr.append("rickroll")


def popLast(arr: list):
    return arr.pop()


while True:
    try:
        courses = []

        appendCourses(courses)

        print(f"Courses: {courses}")

        print(f"The array popped: {popLast(courses)}")
        print(f"The courses: {courses}")
        break
    except Exception as e:
        print(e)
