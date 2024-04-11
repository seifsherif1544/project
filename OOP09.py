class Person():
    def __init__(self) -> None:
        self.firstName = '' # public
        self.lastName = ''
        self._birthYear = 2000 # protected (same class, sub classes)
        self.__nid = '' # private (same class only)


    # def getBirthYear(self):
    #     return self._birthYear

    # def setBirthYear(self, newBirthYear):
    #     if type(newBirthYear) == int and newBirthYear <= 2024:
    #         self._birthYear = newBirthYear
    #     else:
    #         raise Exception("Invalid birth year.")
    
    @property
    def birthYear(self):
        return self._birthYear

    @birthYear.setter
    def birthYear(self, newBirthYear):
        if type(newBirthYear) == int and newBirthYear <= 2024:
            self._birthYear = newBirthYear
        else:
            raise Exception("Invalid birth year.")
        
    def getFullName(self):
        return f"{self.firstName} {self.lastName}"
    
    def getAge(self):
        return 2024 - self._birthYear

class Student(Person):
    def __init__(self) -> None:
        super().__init__()
        self.classRoom = ''
    
class Teacher(Person):
    def __init__(self) -> None:
        super().__init__()
        self.subject = ''
        self.__salary = 1000

    @property
    def salary(self):
        return self._birthYear

    @salary.setter
    def salary(self, newSalary):
        if type(newSalary) == int and newSalary <= 2024:
            self._birthYear = newSalary
        else:
            raise Exception("Invalid salary.")
        
    def x(self):
        self._birthYear = 2001


    

__birthYear = 2005

s = Student()
# s._birthYear = 2023
# s.setBirthYear(2005)
s.birthYear = 'hi' # setter
print(s.getAge())
# print(s.getBirthYear())
print(s.birthYear) # getter

t = Teacher()
t.__salary = 'hi'
