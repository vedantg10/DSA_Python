myDict = {'name': 'Edy', 'age': 26, 'address': 'London'}

def traverseDict(dict):
    for key in dict:                #Time complexity should be O(N) bcoz we are looping
        print(key, dict[key])


traverseDict(myDict)