class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.value)


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1 
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
    def traverse(self):
        current_node = self.head
        result = ""
        while(current_node):
            result += str(current_node.value) + '\n'
            current_node = current_node.next 
        return result

    def __str__(self):
        if self.length == 0:
            return None
        current_node = self.head
        result = ""
        while (current_node):
            result += str(current_node.value)
            if current_node.next is not None:
                result += ' <-> '
            current_node = current_node.next
        return result
    
newDLL = DoublyLinkedList()
newDLL.append(20)
newDLL.append(30)
newDLL.append(40)
newDLL.prepend(90)
print(newDLL.traverse())
    


        
