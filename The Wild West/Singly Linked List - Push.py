# Implement the following on the SinglyLinkedList class:

# push

# This function should take in a value and add o node to the end of the SinglyLinkedList. It should return the SinglyLinkedList.

# Examples

# singlyLinkedList = SinglyLinkedList()
# singlyLinkedList.push(5)  # Success
# singlyLinkedList.length   # 1
# singlyLinkedList.head.val # 5
# singlyLinkedList.tail.val # 5
 
# singlyLinkedList.push(10)    # Success
# singlyLinkedList.length      # 2
# singlyLinkedList.head.val    # 5
# singlyLinkedList.head.next.val  # 10
# singlyLinkedList.tail.val    # 10


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self, data):
        newNode = Node(data)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length +=1
        return "Success"