class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution(object):
    def middleNode(self, head):
        slow_node = head
        fast_node = head
        while(fast_node is not None and fast_node.next is not None):
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        return slow_node

    