'''
Please, enter your first name: _
Please, enter your last name: _
Please, enter your birth year: _2000

==========================================
                   C.V.
------------------------------------------
Your full name: Ahmed Ali
Your age: 23
==========================================
''' 

firstName = input("Please, enter your first name: ")
lastName = input("Please, enter your last name: ")
fullName = firstName + " " + lastName
birthYear = int(input("Please, enter your birth year: "))
age = 2024 - birthYear
width = 80
separatorTopBottom = "="
separatorInbetween = "-"
print(separatorTopBottom * width)
print(" " * int((width - 4) / 2) + "C.V.")
print(separatorInbetween * width)
print("Your full name: " + fullName)
print("Your age: " + str(age))
print(separatorTopBottom * width)

