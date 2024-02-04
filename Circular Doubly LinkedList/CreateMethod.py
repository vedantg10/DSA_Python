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
    
circularDLL = DoublyCircularLinekdList()
print(circularDLL.createCDLL(5))
print([node.value for node in circularDLL])
