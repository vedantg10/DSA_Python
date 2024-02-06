class Solution:
    def partition(self, head:ListNode, x:int) -> ListNode:
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right

        while head:
            if head.val<x:
                ltail.next = head
                ltail =ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next
        
        ltail.next = right.next
        rtail.next = None