from m_reading import readInteger
import m_general as general

class teacher():
    @staticmethod
    def welcomeTeacher(fullName:str):
        print(f"Welcome {fullName}")

    allTeachers = [] # class (member) variable

    @classmethod
    def addTeachers(cls):
        while True:
            t = teacher()
            t.firstName = input("Please, enter your first name: ").strip().capitalize()
            t.lastName = input("Please, enter your last name: ").strip().capitalize()
            t.birthYear = readInteger("Please, enter teacher birth year: ", 1900, general.currentYear) #int(input('Please, enter teacher birth year: '))
            t.basicSalary = readInteger("Basic salary: ", 0, 2000000)
            t.overTime = readInteger("Over time: ", 0, 100000)
            t.discount = readInteger("Discount: ", 0, 100000)

            cls.allTeachers.append(t)

            ask = input("Exist (y/n)? ")
            if ask.strip().lower() == "y":
                break        

    @classmethod
    def printAllTeachers(cls):
        col1, col2, col3 = 50, 6, 14
        width = col1 + col2 + col3
        print("=" * width)
        print(f"{'Full name':<{col1}}{'Age':<{col2}}{'Net salary':>{col3}}")
        for tch in cls.allTeachers: # [t1, t2, t3]
            print("-" * width)
            fullName = tch.fullName()
            age = tch.age()
            netSalary = tch.netSalary()
            print(f"{fullName:<{col1}}{age:<{col2}}{netSalary:>{col3}.2f}")
        print("=" * width)

    def __init__(self) -> None:
        # instance members (variables)
        self.firstName = '' # variables, atrributes, properties, fields -> data
        self.lastName = ''
        self.birthYear = 2000
        self.basicSalary = 1000
        self.overTime = 0
        self.discount = 0

    def fullName(self): # instance member (method)
        return f"{self.firstName} {self.lastName}"
    
    def age(self)->int:
        # return datetime.datetime.today().year - self.birthYear
        return general.currentYear - self.birthYear
    
    def netSalary(self):
        return self.basicSalary + self.overTime - self.discount

def add(n1, n2):
    pass

if __name__ == "__main__": # direct execution
    print('Hi from oop04')

# teacher.addTeachers()
# teacher.printAllTeachers()

'''
===============================================
Full name                   age      net salary
-----------------------------------------------
Ahmed Ali                   35          1200.00
-----------------------------------------------
Mohammed Hassan             37          2000.75
===============================================
'''

