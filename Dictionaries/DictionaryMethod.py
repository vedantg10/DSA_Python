
myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}

dict = myDict.copy()
print(myDict)
print(dict)

newDict = {}.fromkeys([1,2,3],0)
print(newDict)

print(myDict.get('age', 27)) #if the key does not exist in the dict, it will return the value given in the get function

print(myDict.items())

print(myDict.keys())

print(myDict.popitem())

print(myDict.setdefault('name1', 'added'))

print(myDict.values())

newDict = {'a': 1, 'b': 2, 'c': 3}
myDict.update(newDict)
print(myDict)
