# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode()
        carry = 0
        while l1 or l2:
            s = 0
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            s += carry 
            carry = s // 10
            s = s % 10
            prev.next = ListNode(s)
            prev = prev.next
        if carry != 0:
            prev.next = ListNode(carry)
        return dummy.next