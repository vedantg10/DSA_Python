#Update/ add an element to the dictionary

myDict = {"name":'Edy', 'age':26}

myDict['age'] = 27
myDict['name'] = "Vedant" #Time complexity should be O(1), just trying to access the dict
print(myDict)


myDict['address'] = 'Calgary' ##Time complexity should be O(1), just trying to update the dict with new key, value pair