# Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.



# Example 1:

# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next

        prevous_node= None
        current_node = head
        while(current_node):
            if (current_node.val == val):
                prevous_node.next = current_node.next
            else:
                prevous_node = current_node
            current_node = current_node.next
        return head