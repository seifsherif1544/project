class student():
    def __init__(self, first_Name, last_Name) -> None:
        self.firstName = first_Name
        self.lastName = last_Name
        
    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"
    
s1 = student('Mohammed', 'Hassan')
# s1.firstName = 'Ahmed'
# s1.lastName = 'Ali'
print(s1.fullName)

