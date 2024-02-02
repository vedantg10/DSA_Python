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
    
    def reverseTraverse(self):
        current_node = self.tail
        while(current_node):
            print(current_node.value)
            current_node = current_node.prev

    def search(self, val):
        current_node = self.head
        while(current_node):
            if current_node.value == val:
                return True
            current_node = current_node.next
    

    def get(self, index):
        if index <0 or index>= self.length:
            return None
        if index < self.length//2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length -1, index, -1):
                current_node = current_node.prev
        return current_node
    
    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
     
    def insert(self, index, value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return
        if index<0 and index>=self.length:
            return None
        if index == 0:
            self.prepend(value)
        elif index == self.length-1:
            self.append(value)
        else:
            prev_node = None
            current_node = self.head
            for i in range(index):
                prev_node = current_node
                current_node =current_node.next
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = current_node
            current_node.prev = new_node
        self.length += 1

    def popFirst(self):
        if self.length ==1:
            self.head = None
            self.tail = None
        else:
            popped_node = self.head
            self.head = popped_node.next
            self.head.prev = None
            popped_node.next = None
        self.length -=1
        return popped_node
    
    def popMethod(self):
        if self.length ==0:
            return None
        if self.length ==1:
            self.head = None
            self.tail = None
        else:
            propped_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            propped_node.prev = None
        self.length -= 1

    def remove(self, index):
        prev_node = None
        current_node = self.head
        if index<0 and index >= self.length:
            return None
        if self.length ==1:
            self.head = None
            self.tail = None
        elif index == 1:
            self.popFirst()
        elif index == self.length -1:
            self.popMethod()
        else:
            for _ in range(index):
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = current_node.next
            current_node.next.prev = prev_node
            current_node.next = None
            current_node.prev = None
        self.length -=1

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
newDLL.reverseTraverse()
print(newDLL.search(100))
newDLL.set_value(0,100)
newDLL.insert(2,90)
newDLL.popFirst()
newDLL.remove(2)
print(newDLL)
    


        
