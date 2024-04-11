# import datetime
from datetime import datetime

class student():
    def __init__(self) -> None: # constructore
        self.firstName = ''
        self.lastName = ''
        self.birthYear = 2000

    def fullName(self):
        # return f"{self.firstName} {self.lastName}"
        return f"{self.lastName}, {self.firstName}"
    
    def age(self):
        return datetime.today().year - self.birthYear


s1 = student()
s2 = student()
s3 = student()
s4 = student()
s5 = student()



# print(s1.fullName())
s1.firstName = 'Ahmed'
s1.lastName = "Ali"
s1.birthYear = 2003
# print(s1.fullName(), s1.age())

s2.birthYear = 2005
s3.firstName = 'Mohammed'
s3.lastName = "Yousof"
allStudents = [s1, s2, s3, s4, s5]

allStudents = [ ('Ahmed', 'Ali', 25), ('Mohammed', 'Hassan', 22), ('Fatema', 'Yousof', 24) ]

print("=" * 30)
for s in allStudents:
    print(s[0], s[1], s[2])
    # print(s.fullName(), s.age())
print("=" * 30)
# Ali, Ahmed
