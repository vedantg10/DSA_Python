#Accessing/Traversing the list

sampleList = ['item1', 'item2', 'item3', 'item4']

def traverse(sample):
    for item in sample:
        print(item)

traverse(sampleList)

print(sampleList[0])

print('item1' in sampleList) #-----boolean value if it is true or false

print(sampleList[-1]) #--------- -1 stands index of the last element