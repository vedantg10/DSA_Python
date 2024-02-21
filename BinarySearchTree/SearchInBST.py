import QueueUsingLinkedList as queue
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild =None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been successfully inserted"


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    customQueue  = queue.Queue()
    customQueue.enqueue(rootNode.data)
    while not customQueue.isEmpty():
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftChild is not None:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customQueue.enqueue(root.value.rightChild)
            


newBST = BSTNode("Drinks")
print(insertNode(newBST,70))
# leftChild = BSTNode("Cold")
# rightChild = BSTNode("Hot")
# newBST.leftChild = leftChild
# newBST.rightChild = rightChild