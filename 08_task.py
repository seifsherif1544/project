
print("Welcome")


while True:
    startNo = int(input("Please, enter first number: "))
    #endNo = startNo - 1 # int(input("Please, enter last number: "))

    # if startNo > endNo:
    #     print("Invalid")
    # else:    
    #     sum = 0
    #     while startNo <= endNo:
    #         sum = sum + startNo
    #         startNo = startNo + 1
            
    #     print(sum)

    while True: # endNo < startNo: # iteration
        try:
            endNo = int(input("Please, enter last number: "))
        except:
            print("Only number.")
            continue

        if endNo < startNo:
            print("invalid")
        else:
            break
    sum = 0

    while startNo <= endNo:
        sum = sum + startNo
        startNo = startNo + 1
        
    print(sum)

    ask = input("Exit (y/n)? ")
    if ask == 'y':
        break

print("Good bye.")