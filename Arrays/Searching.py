from array import *

my_array = array('i', [1,2,3,4,5])

def linearSearch(array, target):
    for i in range(len(array)):
        if target == array[i]:
            return i
    return -1

print(linearSearch(my_array, 5))
