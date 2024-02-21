class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild =None
        self.rightChild = None


newBST = BSTNode("Drinks")
leftChild = BSTNode("Cold")
rightChild = BSTNode("Hot")
newBST.leftChild = leftChild
newBST.rightChild = rightChild