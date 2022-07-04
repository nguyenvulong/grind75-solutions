"""
Thanks: top answer
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    I modified top answer and use "moving" head instead of "current" pointer
    p will handle the tail at the end, which points to None
    prev keeps track of previous element
    head keeps moving, nxt keep track of the next element, head points back to prev
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = ListNode()
        p.next = head
        
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        if p.next:
            p.next.next = None
