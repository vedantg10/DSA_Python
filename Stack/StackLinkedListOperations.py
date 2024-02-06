class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    
    def push(self, value):
        newNode = Node(value) 
        if self.LinkedList.head == 0:
            self.LinkedList.head = newNode
        else:
            newNode.next = self.LinkedList.head
            self.LinkedList.head = newNode
    
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
    
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
    
    def delete(self):
        self.LinkedList.head ==None



customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
