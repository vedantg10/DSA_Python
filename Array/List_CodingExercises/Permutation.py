def permutation(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    lst1.sort()
    lst2.sort()
    if lst1 == lst2:
        return True
    else:
        return False
    
lst1= [1,2,3]
lst2 = [1,3,2]
print(permutation(lst1, lst2))