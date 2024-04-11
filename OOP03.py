from datetime import datetime
from OOP04 import teacher as newTeacher, add

newTeacher.addTeachers()
newTeacher.printAllTeachers()

# t1 = newTeacher()
# t1.birthYear = 2003
# print(t1.age())

exit()


class teacher():
    def __init__(self) -> None: # constructore
        self.firstName = ''
        self.lastName = ''
        self.birthYear = 2000
        self.basicSalary = 1000
        self.overTime = 0

    def fullName(self):
        # return f"{self.firstName} {self.lastName}"
        return f"{self.lastName}, {self.firstName}"
    
    def age(self):
        return datetime.today().year - self.birthYear


allTeachers = []

while True:
    s = teacher() # object, instance
    s.firstName = input("Please, ene")

    allTeachers.append(s)
    ask = input("Exit (y/n)? ")
    if ask == "y":
        break


for x in allTeachers:
    print(f"{x.fullName():<25} {x.age():<4} {x.netSalary():>15.2f}")
    print("-" * 41)

'''
===============================================
Full name                   age      net salary
-----------------------------------------------
Ahmed Ali                   35          1200.00
-----------------------------------------------
Mohammed Hassan             37          2000.75
===============================================
'''