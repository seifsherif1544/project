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




def add(n1:int, n2:int)->int:
    return n1 + n2
    
# print(add(3, 5)) # actual result, expected result
# print(add(-3, -5))
# print(add(-3, 5))
