myList = ['a', 'b', 'c', 'd', 'e', 'f']

print (myList[0:2])
print (myList[:])

myList[0:2] = ['h', 'z']

print(myList)

#Deletion

myList.pop(1)
print(myList)

del myList[3]
print (myList)

del myList[2:3]

myList.remove('h')
print(myList)

#### concatenation using + ########

a = [1,2,3]
b = [4,5,6]
c = a + b
print (c)

###### elements in list repeated using * ######

a = [0,1]
a = a*3
print(a)

######### max() and min() ####

print (max(a))
print (min(a))

######## sum() ########

a = [0,1,2,3,4,5]
print (sum(a))


# total = 0
# count = 0
# while(True):
#     inp = input('Enter the number: ')
#     if inp == 'done':break
#     value = float(inp)
#     total = value + total
#     count = count +1
#     average = total/count
# print ('Average:', average)

# ########### average using list ##############

# sumList = []
# while(True):
#     inp = int(input('Enter the number: '))
#     if inp == -1:break
#     sumList.append(inp)
#     average = sum(sumList)/len(sumList)
# print ('Average:', average)



################## character into list from the word ########

a = 'spam'
b = list(a)
print(b)

a = 'spam-spam-spam'
b = a.split('-')
print(b)