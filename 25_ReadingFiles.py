# myFile = open(r"folder1\MyData.txt", 'a') # for reading

# # allText = myFile.read()
# # print(allText)
# myFile.write("\nnew data 004" * 5)
# myFile.close()

# Comma Separated Values
myFile = open(r"folder1\MyData.txt", 'r')
allText = myFile.readlines()
print(allText)
for line in allText:
    data = line.strip('\n') .split(',') # ["Ahmed", "Ali", "25", "Cairo"]
    fullName = f"{data[0]} {data[1]}"
    print(f"{fullName:<25} {data[2]:3} {data[3]:>15}")
    # print(line)

# print(allText)
