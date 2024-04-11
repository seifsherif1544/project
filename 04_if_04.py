
firstName = ''
lastName = 'Ali'
nationalID = '12345678901234'
age = -3


if nationalID or (firstName and lastName):
    print('Yes')
else:
    print("no")


if firstName and (lastName or nationalID):
    print("yes")

