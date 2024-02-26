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


preOrderTraversal(newAVlTree)


