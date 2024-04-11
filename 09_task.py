# mutable vs immutable

x = 0
print(id(x))
x = 1
print(id(x))

firstName = 'Ahmed'
print(id(firstName))
# firstName[0] = 'a'

firstName = 'ahmed'
print(id(firstName))

exit()

start = int (input("Please, enter first number: "))
end = int (input("Please, enter last number: "))

n1 = int(input("Please, enter divider1: "))
n2 = int(input("Please, enter divider2: "))

sum = 0

for x in range(start, end + 1):
    if x % n1 == 0 or x % n2 == 0:
        sum += x

# for x in range(start, end + 1):
#     if x % n1 == 0 and x % n2 == 0:
#         sum += x

print(sum)

# 5,6,7,8,9