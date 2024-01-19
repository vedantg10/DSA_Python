def pair_sum(myList, sum):
    pairs_list = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sum:
                pairs_list.append(f"{myList[i]}+{myList[j]}")
    return pairs_list

print (pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))