# OOP Concepts
# 1) Inheritance التوريث
# 2) Encapsulation التغليف
# 3) Polymorphism التعددية الشكلية   
#       a) overloading  b) overriding
# 4) Abstraction التجرد

import m_general as general

class person(): # parent, base, super
    def __init__(self) -> None:
        self.firstName = '' 
        self.lastName = ''
        self.__birthYear = 2000 # private
        self.tel = ''
        self.nid = ''

    def setBirthYear(self, newBirthYear):
        self.__birthYear = newBirthYear

    def getBirthYear(self):
        return self.__birthYear

    def fullName(self): # instance member (method)
        # return f"{self.firstName} {self.lastName}" # bug -> debug
        return f"{self.lastName}, {self.firstName}" # bug -> debug
    
    def age(self)->int:
        # return datetime.datetime.today().year - self.birthYear
        return general.currentYear - self.__birthYear
    
    def printData(self):
        raise NotImplementedError('Please, dfsd')

class workingPerson(person):
    def __init__(self) -> None:
        super().__init__()
        self.basicSalary = 1000
        self.overTime = 0
        self.discount = 0
        

    def netSalary(self):
        return self.basicSalary + self.overTime - self.discount

class employee(workingPerson): # child, derived, sub
    def __init__(self) -> None:
        super().__init__()
        self.departement = ''

    def printData(self):
        return "This is employee"

e = employee()
# e.__birthYear = 'hi'
e.setBirthYear('Hi')
print(e.getBirthYear())


class teacher(workingPerson):
    def __init__(self) -> None:
        super().__init__()        
        self.subject = ''

    def printData(self):
        return "This is teacher"
    
t = teacher()
t.firstName = 'Ahmed'
t.lastName = 'Ali'
print(t.fullName())
print(t.printData())

class student(person):
    def __init__(self) -> None:
        super().__init__()
        self.classRoom = ''
        self.degree = 0

    def fullName(self): # instance member (method)
        # return f"{self.firstName} {self.lastName}" # bug -> debug
        return f"{self.firstName} {self.lastName}" # bug -> debug
    
    def printData(self):
        return "this is student data"


s = student()
s.firstName = 'Mohammed'
s.lastName = 'Hassan'
print(s.fullName())
print(s.printData())
