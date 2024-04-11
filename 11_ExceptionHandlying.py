
# 1) Syntax error
# 2) Runtime error
# 3) Logical error

# price = float(input("Please, enter price: "))
# qty = float(input("Please, enter quantity: "))
# total = price * qty

counter = 1
while True:

    if counter >= 3:
        print("Game over")
        break
    counter += 1

while True:
    try:
        salary = float(input("Please, enter your salary: "))
    except:
        print("Only numbers.")
        continue

    if salary < 0:
        print("Salary should be greater than 0.")
    else:
        break

print(salary)

try:
    print("1")
    n1 = int(input())
    n2 = int(input())
    result = n1 / n2
    print("2")
except ValueError as ex:
    print("Only numbers.", ex)
except ZeroDivisionError as ex1:
    print("Can not divide by zero", ex1)
except:
    print("Invalid")

print("Good bye.")

