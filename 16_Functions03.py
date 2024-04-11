
def readInteger(msg:str, start:int = -1000000000, end:int = 1000000000)->float:
    while True:
        try:
            value = int(input(msg)) # 400
            if value < start or value > end:
                print("Value should be between " + str(start) + " and " + str(end) )
            else:               
                return value
        except:
            print("Invalid")


age = readInteger("Please, enter your age: ")
salary = readInteger("Please, enter your salary: ", 1000, 25000)
experience = readInteger("Please, enter your years of experience: ", 0, 30)
revenues = readInteger("pelsa")

'''
['ahmed', 'mohammed']

================== 25
|Ahmed           |
|Mohammed        |
|x               |
==================
'''

print(age, salary, experience)

# while True:
#     try:
#         salary = int( input("Please, fsdfsdf: ")) # -600
#         if salary < 0:
#             print("Salary should be greater than 0")
#             continue
#         break
#     except:
#         print("Invalid")
