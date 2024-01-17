# Write a function to find the missing number in a given integer array of 1 to 100. 
# The function takes to parameter the array and the number of elements that needs to be in array.  
# For example if we want to find missing number from 1 to 6 the second parameter will be 6.

# solution1: 

def missing_number(array, n):
    for i in range(1,n):
        if i not in array:
            return i 
        

missing_number([1,2,3,4,6], 6)

# solution2:

def missing_number1(arr, n):
    total = n*(n+1)/2
    sum_arr = sum(arr)
    missing = total-sum_arr
    return missing

print(missing_number1([1,2,3,4,6,7], 7))

#solution 2 will fail if there are more than 1 integer missing in the array