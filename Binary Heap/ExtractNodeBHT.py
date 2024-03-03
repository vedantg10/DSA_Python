class Heap():
    def __init__(self, size):
        self.customList = (size+1) *[None]
        self.heapSize = 0
        self.maxSize = size+1


def peakofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]
    
def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize


def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1,rootNode.heapSize+1):
            print(rootNode.customList[i])

def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <=1:
        return 
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)


def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize +1 == rootNode.maxSize:
        return "The Binary heap is full"
    rootNode.customList[rootNode.heapSize+1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been successfully inserted"


def heapifyTreeExtrat(rootNode, index, heapType):
    leftIndex = index*2
    rightIndex = index*2 +1
    swapChild = 0

    if rootNode.heapSize <leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp


newBinaryHeap = Heap(5)
print(sizeofHeap(newBinaryHeap))
insertNode(newBinaryHeap, 4, "Max")
insertNode(newBinaryHeap, 5, "Max")
insertNode(newBinaryHeap, 2, "Max")
insertNode(newBinaryHeap, 1, "Max")
levelOrder(newBinaryHeap)