import QueueUsingLinkedList as queue
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def searchBT(rootNode, nodeValue):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if(root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if(root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Not found"

print(searchBT(newBT, "Hot"))



    
