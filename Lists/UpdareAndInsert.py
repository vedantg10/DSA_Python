#Update/Insert - List

myList = [1,2,3,4,5,6,7]
myList[3] = 33
print(myList)      #-------- time complexity for updating O(1)


myList.insert(0, 55)
myList.append('item')
print(myList)

newList = [11,12,23,24]
myList.extend(newList)

print(myList)