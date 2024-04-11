degree = 90

if degree < 0 or degree > 100:
    print("Value should be between 0 and 100.")
elif degree < 50:
    print("Sorry, fail.")
elif degree < 65:
    print("fsdfs")
    print("Pass.")
elif degree < 75:
    print("fsdfs")
    print("Good.")
elif degree < 85:
    print("sdfsdf")
    print("Very good.")
elif degree <= 100:
    print("fsdf")
    print("Excellent.")
else:
    print("Invalid")

if degree >= 0 and degree <= 100: # valid range 0, 1, 2, ....... 99, 100
    if degree < 50:
        print("Sorry, fail.")
    else:
        print("Congraa")
        if degree < 65:
            print("Pass.")
        elif degree < 75:
            print("Good.")
        elif degree < 85:
            print("Very good.")
        elif degree <= 100:
            print("Excellent.")    

    if degree >= 50:
        print("Congraa")
        if degree < 65:
            print("Pass.")
        elif degree < 75:
            print("Good.")
        elif degree < 85:
            print("Very good.")
        elif degree <= 100:
            print("Excellent.")    
    else:
        print("Sorry, fail.")
else:
    print("Value should be between 0 and 100.")

