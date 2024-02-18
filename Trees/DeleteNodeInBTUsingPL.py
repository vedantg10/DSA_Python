class BinaryTree():
    def __init__(self, size):
        self.customList = size*[None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex+1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"
    
    def searchNode(self, value):
        current_pointer = 0
        if self.customList == None:
            return "No element in the List"
        while (current_pointer+1 != self.maxSize):
            if self.customList[current_pointer+1] == value:
                return "Success"
            current_pointer +=1
        return "Not found"
    
    def preOrderTraversal(self, index):
        if index> self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2+1)

    def postOrderTraversal(self, index):
        if index> self.lastUsedIndex:
            return
        self.preOrderTraversal(index*2)
        self.postOrderTraversal(index*2 +1)
        print(self.customList[index])
    
    def inOrderTraversal(self, index):
        if index> self.lastUsedIndex:
            return
        self.preOrderTraversal(index*2)
        print(self.customList[index])
        self.postOrderTraversal(index*2 +1)

    def levelOrderTraversal(self, index):
        if index>self.lastUsedIndex:
            return
        print(self.customList[index])
        self.levelOrderTraversal(index+1)

    def deleteNode(self, nodeVal):
        if self.lastUsedIndex ==0:
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == nodeVal:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -=1
                return "The node has been suceessfully deleted"
    
    def deleteBT(self):
        self.customList = None
        return "The BT has been successfully deleted"


newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
newBT.levelOrderTraversal(1)
