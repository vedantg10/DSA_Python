from array import *

my_array = array('i', [1,2,3,4,5])

my_array.remove(4)
print(my_array)

##time complexity depends on the operation, if last element deleted then it is O(1), otherwise O(n)