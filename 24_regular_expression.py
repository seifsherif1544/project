import re

email = "asfs@fasd.comnetinfo"
tel = "01012345678" # input('Please, enter your tel: ')
carNo = "3-3, 2-4, 3-4" # abc123, ab1234, abc1234

result = re.match(r"^01[0125]\d{8}$", tel)
result2 = re.search(r"^01[0125]\d{8}$", tel)

if result:
    print("yes tel 1")
else:
    print("No tel 1")

if result2:
    print("yes tel 2")
else:
    print("No tel 2")