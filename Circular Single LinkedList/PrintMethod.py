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


CircularlinkedList = CSlinkedList(10)
CircularlinkedList.append(10)
CircularlinkedList.append(20)
CircularlinkedList.append(30)
print(CircularlinkedList)
