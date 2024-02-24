
# Singly Linked List - Rotate
# Implement the following on the SinglyLinkedList class:

# Rotate

# This function should rotate all the nodes in the list by some number passed in. For instance, if your list looks like 1 -> 2 -> 3 -> 4 -> 5 and you rotate by 2, the list should be modified to 3 -> 4 -> 5 -> 1 -> 2. The number passed in  to rotate can be any integer.

# Time Complexity : O(N), where N is the length of the list.

# Space Complexity : O(1)


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
        
    def rotate(self, number):
        index =  (number + self.length) if number < 0 else number
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return "No Rotation"
        prevNode = self.head
        for i in range(index-1):
            prevNode = prevNode.next
        if prevNode == None:
            return "No Rotation"
        self.tail.next = self.head
        self.head = prevNode.next
        self.tail = prevNode
        prevNode.next = None
        return "Success"
        # TODO