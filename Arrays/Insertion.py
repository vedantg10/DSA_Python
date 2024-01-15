from array import *

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.3,1.5,1.6])

#print(arr2)

# arr1.insert(2,9)
# print(arr1)

def traverseArray(array):
    for element in array:
        print (element)

traverseArray(arr1)

#time complexity of the above code will O(n)


###Access array element####


def accessElement(array, index):
    if index> len(array): #--------------------- O(1)
        print ('There is not any element in this index') #-----------------O(1)
    else:
        print (array[index]) #-------------O(1)

accessElement(arr1, 3)

### time complexity for the above is O(1)

