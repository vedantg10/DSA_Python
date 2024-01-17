my_list = [1,2,3,9,9,8]
def first_second(my_list):
    max1, max2 = float('-inf'), float('-inf')
    
    for num in my_list:
        if num> max1:
            max1 = num
            max2 = max1
        elif num>max2 and num !=max1 and num != max2:
            max2 = num
    return max1, max2

print(first_second(my_list))