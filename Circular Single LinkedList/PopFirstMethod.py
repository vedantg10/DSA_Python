class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class CSlinkedList():
    def __init__(self, value):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        if self.head is None:
            return None
        current_node = self.head
        result = ""
        while current_node is not None:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
            result =  result + '->'
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
            # new_node = self.head
        self.length += 1

    def insert(self, value, index):
        new_node = Node(value)
        if index >self.length or index <0:
            raise Exception('Index out of range')
        if index == 0:
            new_node.next = self.head
            self.tail.next = new_node
            self.head  = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        elif index>0:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length +=1 
    
    def traversal(self):
        current_node = self.head
        result = ''
        while current_node is not None:
            result += str(current_node.value) +'\n'
            current_node = current_node.next
            if current_node == self.head:
                break
        return result
 
    def search(self, target):
        temp_node = self.head
        while(temp_node):
            if temp_node.value == target:
                return True
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return False
    
    def get(self, index):
        if index == -1:
            return self.tail
        if index>self.length or index < -1:
            return None
        for _ in range(index):
            current = current.next
        return current.value
    
        
    def pop(self):
        if self.length ==0:
            return None
        if self.length ==1:
            self.head = self.tail = None
        else:

            prev_node = None
            current_node = self.head
            while(current_node != self.tail):
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = self.head
            self.tail = prev_node
            current_node.next = None
            self.length -= 1

    def popFirst(self):
        if self.length ==0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            popped_node = self.head
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node



CircularlinkedList = CSlinkedList(10)
CircularlinkedList.append(10)
CircularlinkedList.append(20)
CircularlinkedList.append(30)
CircularlinkedList.append(100)
CircularlinkedList.append(10)
print(CircularlinkedList)
CircularlinkedList.pop()
print(CircularlinkedList)


