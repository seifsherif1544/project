
start = 1 # int(input("Please, enter start: "))
end = 6 # int(input("Please, enter end: "))

sum = 0
for x in range(start, end + 1):
    if x % 2 > 0:
        continue

    # sum = sum + x
    sum += x
    
print(sum)

