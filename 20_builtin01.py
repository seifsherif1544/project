allNames = ['ahmed', ' aLi', ' MohAMmEd    ']

def removeSpacesAndCapitalize(origin:str):
    return origin.strip().capitalize()

print(allNames)
newList = list( map(removeSpacesAndCapitalize, allNames ) )
print( newList )
print(allNames)

allSalaries = [1200, 600, 0, 1100, 2200, 850]

# print( len(allSalaries) )
print( max(allSalaries) )
# print( min(allSalaries) )
# print( sum(allSalaries) )
# print( sum(allSalaries) / len(allSalaries) )
# print( id(allSalaries) )
# allSalaries.append(700)
# print( id(allSalaries) )
# print( type(0.0) )

# if any(allSalaries):
#     print("Yes")
# else:
#     print("No")
