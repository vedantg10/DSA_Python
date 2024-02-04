
from linkedlist import LinkedList

def remove_duplicates(ll):
    if ll.head is None:
        return
    current_node = ll.head
    while(current_node is not None and current_node.next is not None):
        if current_node.value == current_node.next.value:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
    return ll.head
            