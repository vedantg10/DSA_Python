class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = None
        self.tail =None
        self.length = 0
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
        else:
            pass
        self.length += 1 
