def max_product(arr):
    max1, max2 =0,0
    for num in arr:
        if num > max1:
            max1 = num
            max1 = max2
        elif num>max2:
            max2 = num
    