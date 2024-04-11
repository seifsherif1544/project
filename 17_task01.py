'''
['ahmed', 'mohammed']

================== 25
|Ahmed           |
|Mohammed        |
|x               |
==================
'''
def printNames(source:list):
    width = 60
    sep = "#"
    verticalSep = "|"    
    subtraction = len(verticalSep) * 2

    print(sep * width)

    for name in source:
        name = str(name)
        print(verticalSep + name.ljust(width - subtraction) + verticalSep)
    
    print(sep * width)

def removeSpacesAndCapitalize(origin:str):
    return origin.strip().capitalize()


def addStudents() ->list:
    allNames = []

    while True:
        newName = removeSpacesAndCapitalize( input("Please, enter student name: ") )

        if newName: # '' othewise true
            allNames.append(newName)
            ask = input("Exit (y/n)? ")
            if ask.strip().lower() == "y": # Y
                break
    return allNames
    

myListOfStudents = ["Ahmed", "Mohammed", "Ali"] # addStudents()
printNames(myListOfStudents)

