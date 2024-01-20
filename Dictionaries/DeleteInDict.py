#Delete an Element from Dictionary

myDict = {'name': 'Edy', 'age': 26, 'address': 'London'}

del myDict['age']
print(myDict)

myDict.pop('name')
print(myDict)

myDict.popitem()
print(myDict)
