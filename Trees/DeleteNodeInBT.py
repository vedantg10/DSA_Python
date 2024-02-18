import QueueUsingLinkedList as queue

class Tree:
    def __init__(self, data):
        self.data =data
        self.leftChild = None
        self.rightChild = None


newBT = Tree("Drinks")
leftChild = Tree("Cold")
rightChild = Tree("Hot")
newBT.leftChild = leftChild
newBT.rightChild = rightChild


def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print("LOT output " + root.value.data)
            if(root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if(root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print("LOT output " + root.value.data)
            if(root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if(root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)


def deleteNode(rootNode, node):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"
            if(root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if(root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete"


deepestNode = getDeepestNode(newBT)
deleteDeepestNode(newBT, newBT)
levelOrderTraversal(newBT)




