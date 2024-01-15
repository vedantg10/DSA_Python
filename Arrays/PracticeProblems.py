#1. Create an array and traverse
print('Question 1')
from array import *
myarr = array('i', [1,2,3,4,5])
print (myarr)

def traverse(array):
    for element in array:
        print (element)

traverse(myarr)

#2. Access individual elemenrs through indexes
print('Question 2')
def accessElements(array, index):
    if index> len(array):
        print ("Index out of range")
    else:
        print (array[index])

accessElements(myarr, 4)

#3. Append any value to the array using append() method
print('Question 3')
myarr.append(7)
print (myarr)

#4. Insert value in an array using insert() method
print('Question 4')
myarr.insert(6, 19)
print(myarr)

#5. Extend python array uisng extend() method
print('Question 5')
myarr1 = array('i', [8,9,10,11])
myarr.extend(myarr1)
print(myarr)

#6. Add items from the list into array using fromlist() method
print('Question 6')
tempList = [20,21,22]
myarr.fromlist(tempList)
print(myarr)

#7. Remocve any array element using remove() method

print('Question 7')
myarr.remove(20)
print(myarr)

#8. Remove last array element using pop() method

print('Question 8')
myarr.pop()
print(myarr)

#9. fetch any element through its index using index() method

print('Question 9')
print(myarr.index(21))

#10. Reverse a python array using reverse() method
print('Question 10')
myarr.reverse()
print(myarr)

#11. Get array buffer information thriugh buffer_info() method
print('Question 11')
print(myarr.buffer_info())

#12. Check for number of occurances of an element using count() method
print('Question 12')
print(myarr.count(1))

#13. Convert array to string using tostring() method
print('Question 13')
# strTemp = myarr.tostring()
# print(strTemp)

#14. Convert array to a python list with same elements using tolist() method
print('Question 14')
print(myarr.tolist())

#16. Slice elements form an array
print('Question 16')
print(myarr[1:4])


