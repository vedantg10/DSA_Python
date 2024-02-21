
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



newBST = BSTNode("Drinks")
print(insertNode(newBST,70))
# leftChild = BSTNode("Cold")
# rightChild = BSTNode("Hot")
# newBST.leftChild = leftChild
# newBST.rightChild = rightChild