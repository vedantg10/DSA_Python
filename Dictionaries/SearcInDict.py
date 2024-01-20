myDict = {'name': 'Edy', 'age': 26, 'address': 'London'}

def searchElement(dict, value):
    for key in myDict:
        if dict[key] == value:         #time complexity will be O(N)
            return key, value
    return 'The value does not exist'

print(searchElement(myDict, 26))
