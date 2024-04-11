# 2.7 ─> 3.x
from m_formating import removeSpacesAndCapitalize
from datetime import date
currentYear = date.today().year


firstName, lastName, birthYear, address, salary = 'aHMeD', 'aLi', 2000, 'Cairo', 2200.75
age = currentYear - birthYear

# Your first name is: Ahmed, your last name is: Ali, your full name is Ahmed Ali, your age is 24 years, you get 2200.75 $.
colSalaryWidth = 10.2
firstName = removeSpacesAndCapitalize(firstName) #firstName.strip().capitalize()
lastName = removeSpacesAndCapitalize(lastName) #lastName.strip().capitalize()

print("Your first name is: " + firstName + ", your last name is: " + lastName + ", your full name is " + firstName + " " + lastName + ", your age")
print(f"Your first name is: \033[92m{firstName:<15}\033[0m, your last name is: {lastName}, your full name is {firstName} {lastName}, your age is {age} years, you get \033[93m{salary:>{colSalaryWidth}f}\033[0m $.")
print("Your first name is: {}, your last name is: {}, your full name is {} {}, your age is {} years, you get \033[93m{}\033[0m $.".format(firstName, lastName, firstName, lastName, age, salary))
print("Your first name is: {0:>10}, your last name is: {1}, your full name is {0} {1}, your age is {2} years, you get \033[93m{3}\033[0m $.".format(firstName, lastName, age, salary))
print("Your first name is: {1}, your last name is: {2}, your full name is {1} {2}, your age is {0} years, you get \033[93m{3}\033[0m $.".format(age, firstName, lastName, salary))

# print(f"Your first name is: {firstName:>15}, your last name is: {lastName}, your full name is {firstName} {lastName}, your age is {age} years, you get \033[93m{salary:<{colSalaryWidth}f}\033[0m $.")
# print(f"Your first name is: {firstName:^15}, your last name is: {lastName}, your full name is {firstName} {lastName}, your age is {age} years, you get \033[93m{salary:^{colSalaryWidth}f}\033[0m $.")

width = 70
print(f"┌{'─' * (width-2) }┐")
print(f"│{'Egypt':^{width-2}}│")
print(f"└{'─' * (width-2) }┘")

print('\033[93;42mHello world\033[0m')
'''
-------------------------------------------
Full name                    Age     Salary
-------------------------------------------
Mohammed Abdel Hakeem         22    1300.00
-------------------------------------------
Ahmed Ali                     25     900.55
-------------------------------------------
x y                           28  120000.30
-------------------------------------------

┌───────────────────────────────────┐

─ ┌ ┬ ┐ └ ┴ ┘ │ ├ ┼ ┤

print('\033[93;42mHello world\033[0m')

width = 70
print(f"┌{'─' * (width─2) }┐")
print(f"│{'Egypt':^{width─2}}│")
print(f"└{'─' * (width─2) }┘")
'''

