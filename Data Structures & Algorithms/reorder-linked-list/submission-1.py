# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        sec, rev = slow.next, None
        slow.next = None
        while sec:
            temp = sec.next
            sec.next = rev
            rev = sec
            sec = temp 
        
        cur = head
        while rev:
            cur_next, rev_next = cur.next, rev.next
            cur.next = rev
            rev.next = cur_next
            cur, rev = cur_next, rev_next
        


        
