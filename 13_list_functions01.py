
allSalaries = [2300, 2500, 950, 15000, 950, 1200]

print(allSalaries)
# allSalaries.append([7, 8, 9])
# print( allSalaries.count(950) )
# print( allSalaries.index(2500, -1, 0) ) # []
# allSalaries.clear()

# allSalaries.insert(2, [7, 8, 9])
# allSalaries.extend([7, 8, 9])
# value = allSalaries.pop(2)
# print(value)
# allSalaries.remove(9505)
# allSalaries.reverse()
newList = allSalaries .copy()
# [2300, 2500, 950, 15000, 950, 1200]       [2300, 2500, 950, 15000, 950, 1200]
allSalaries.clear()
# []       [2300, 2500, 950, 15000, 950, 1200]
newList.sort(reverse=True)
# []       [15000, 2500, 2300, 1200, 950, 950]

print(allSalaries)
print(newList)

# Exit?(y/n) y, Y,    y  ,    Y    
