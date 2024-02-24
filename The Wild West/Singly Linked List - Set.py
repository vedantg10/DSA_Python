# Singly Linked List - Set
# Implement the following on the SinglyLinkedList class:

# Set

# This function should accept an index and a value and update the value of the node in the SinglyLinkedList at the index with new value. It should return true if the node is updated successfully or false if an invalid index is passed in.



#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Singly Linked List

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
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
        return "Success"
    
    def set(self, index, value):
        current_node = self.head
        if index<0 and index>=self.length:
            return False
        elif index ==0:
            self.head.val = value
            return True
        elif index == self.length-1:
            self.tail.val = value
        else:
            for _ in range(index):
                current_node = current_node.next
                if current_node == None:
                    return False
            
            current_node.val = value
        return True
    