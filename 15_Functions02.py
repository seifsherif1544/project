

def add(n1, n2, operation):
    welcome('Ahmed')
    if operation == '+':
        return n1 + n2
    elif operation == '*':
        return n1 * n2
    

    # return 0


def welcome(name):
    print("Welcome " + name)

def getfullname(firstName, lastName):
    return firstName + " " + lastName

result = add(4, 6, '+')
# print(result)
# result = add(390, 210, '+')
# result = add(5, 90, '*')

# welcome('Ahmed')
# welcome('Ali')
# welcome('Mohamed')

fullName = getfullname("Ahmed", "Ali")
print(fullName)
fullName = getfullname("Mohammed", "Hassan")
print(fullName)
fullName = getfullname("Yousof", "Fathy")
print(fullName)
