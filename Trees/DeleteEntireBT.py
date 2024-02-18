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


def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted"