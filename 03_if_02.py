
print("Starting..")
degree = 23000

if degree < 0:
    print("Value should be between 0 and 100.")
elif degree < 50:
    print("Sorry, fail.")
elif degree < 65:
    print("Pass.")
elif degree < 75:
    print("Good.")
elif degree < 85:
    print("Very good.")
elif degree <= 100:
    print("Excellent.")
else:
    print("Invalid")

if degree < 0:
    print("Invalid")
    
else:
    if degree < 50:
        print("Sorry, fail.")
    else:
        if degree < 65: # nested if
            print("Pass")
        else:
            if degree < 75:
                print("Good")
            else:
                if degree < 85:
                    print("Very good")
                else:
                    if degree <= 100:
                        print("Excellent")
                    else:
                        print("invalid")

print("End.")


'''
1- Pizza
2- Juice
3- Exit
Please, choose: _
You choosed Pizza
'''

print("1- Pizza")
print("2- Juice")
print("3- Exit")

# choice = input("Please, choose: ")

# if choice == "1":
#     print("You choosed Pizza.")
# elif choice == "2":
#     print("You choosed Juice.")
# elif choice == "3":
#     print("Thank you, good bye.")
# else:
#     print("Invalid choice.")