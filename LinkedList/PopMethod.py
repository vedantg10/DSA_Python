class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def insert(self, index, value):
        new_node = Node(value)
        if index <0 or index >self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        if self.length ==0:
            return None
        popped_node = self.head
        if self.length ==1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node 
    
    def pop(self):
        if self.length ==1:
            self.tail =None
            self.head = None
        else:
            temp = self.head
            while (temp.next is not self.tail):
                temp = temp.next
            self.tail = temp
            self.tail.next = None
        self.length -=1

    
    def remove(self, index):
        if index>= self.length or index<0:
            return None
        if index ==0:
            return self.pop_first
        elif index == self.length:
            return self.pop
        else:
            prev_node = self.get(index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
        self.length -=1
        return popped_node



    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result



new_linked_List = LinkedList()
new_linked_List.prepend(10)
new_linked_List.prepend(20)
new_linked_List.prepend(30)
new_linked_List.append(50)
new_linked_List.insert(2,60)
new_linked_List.traverse()
print (new_linked_List)
print(new_linked_List.set_value(2,50))
print(new_linked_List)


