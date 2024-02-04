class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyCircularLinekdList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    

    def createCDLL(self, nodeValue):
        new_node = Node(nodeValue)
        self.head = new_node
        self.tail = new_node
        new_node.prev = new_node
        new_node.next = new_node
        self.length += 1 
        return "CDLL is created sucessfully"
    
    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            newNode = Node(value)
            if location ==0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location ==1:
                newNode.next = self.head
                newNode.prev = self.head
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index<location-1:
                    tempNode = tempNode.next
                    index +=1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
        return "The node has been successfully insert"
    
    def traversalCDLL(self):
        if self.head is None:
            print("There is not any node for traversal")
        else:
            tempNode = self.head
            while(tempNode):
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode =tempNode.next

    
circularDLL = DoublyCircularLinekdList()
print(circularDLL.createCDLL(5))
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
print([node.value for node in circularDLL])
circularDLL.traversalCDLL()
