

fristName = input("Please, fsdfsdf: ")
lastName = input("Please, fsdfsdf: ")

while True:
    try:
        age = int(input("Please, fsdfsdf: ")) # 400
        if age < 0 or age > 120:
            print("Age should be greater between 0 and ")
            continue
        break
    except:
        print("Invalid")

while True:
    try:
        salary = int( input("Please, fsdfsdf: ")) # -600
        if salary < 0:
            print("Salary should be greater than 0")
            continue
        break
    except:
        print("Invalid")

while True:
    try:
        experience = int( input("Please, ,dfsdfs"))
        break
    except:
        print("Invalid")
    
address = input("Please enter your address: ")