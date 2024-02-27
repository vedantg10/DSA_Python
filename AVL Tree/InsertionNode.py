import QueueUsingLinkedList as queue

class AVLNode():
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


newAVlTree = AVLNode(10)
newAVlTree.leftChild = AVLNode("Hot")
newAVlTree.rightChild = AVLNode("Cold")

def preOrderTraversal(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if rootNode is None:
        return
    preOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    preOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if rootNode is None:
        return
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode.data)
    while not customQueue.isEmpty():
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftChild is not None:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customQueue.enqueue(root.value.rightChild)


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1+max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.righChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1+max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight((rootNode.leftChild) - getHeight(rootNode.rightChild))

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    
    rootNode.height = 1 +max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance >1 and nodeValue <rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance>1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance<-1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
    if balance <-1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode


preOrderTraversal(newAVlTree)


