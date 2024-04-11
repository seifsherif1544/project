
while salary < 0:
    salary = float(input("Please, enter your salary: "))

    if salary < 0:
        print("Invalid salary")        

print(salary)

while True:
    salary = float(input("Please, enter your salary: "))

    if salary < 0:
        print("Invalid salary")
    else:
        break
    
print(salary)



while True:
    firstName = input("Please, enter your first name: ")

    if firstName: 
        break

print(firstName)