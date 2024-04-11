# def add(n1:int, n2:int)->int:
#     return n1 + n2

# def add1(n1:int, n2:int, n3:int)->int:
#     return n1 + n2 + n3

# total = add(5, 7)
# print(total)

def addAny(*numbers:int)->int:
    sum = 0
    for x in numbers:
        sum += x
    
    return sum

def concatenate(*names:str)->str:
    result = ""
    for x in names:
        result += x
    
    return result

# t = addAny(5, 3, 6, 7, 8, 1) #(5, 3, 6, 7, 8, 1) -> packing
# print(t)

r = concatenate('a', 'b', 'c') #('a', 'b', 'c')
print(r)