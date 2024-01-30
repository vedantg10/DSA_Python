class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class CSlinkedList():
    def __init__(self, value):
        self.head = None
        self.tail = None
        self.length = 0

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


CircularlinkedList = CSlinkedList(10)
CircularlinkedList.append(10)
CircularlinkedList.append(20)
print(CircularlinkedList.length)
