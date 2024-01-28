class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        def reverseList(head):
            pre_node = None
            current_node = head
            while current_node is not None:
                temp = current_node.next
                current_node.next = pre_node
                pre_node = current_node
                current_node = temp
            return pre_node

        def middleNode(head):
            slow_pointer = head
            fast_pointer = head
            while fast_pointer is not None and fast_pointer.next is not None:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next
            return slow_pointer

        if head is None or head.next is None:
            return True

        reversed_second_half = reverseList(middleNode(head))

        while reversed_second_half:
            if head.val != reversed_second_half.val:
                return False
            head = head.next
            reversed_second_half = reversed_second_half.next

        return True
