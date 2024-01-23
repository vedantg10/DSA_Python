
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(Self,value):
        new_node = Node(value)
        Self.head = new_node
        Self.tail = new_node
        Self.length = 1

new_linked_list = LinkedList(10)
print(new_linked_list.head.value)