"""
There is a cycle in a linked list if there is some node in the list
that can be reached again by continuously following the next pointer
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
            
    
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        eventually fast and slow would be identical at some point if there is a cycle
        """
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

class Solution_dangerous:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        This answer destroys the linked list
        We simply pass through once and "break" the link at each step. 
        If we have broken the link then there is a cycle.
        """
        try:
            while True:
                if head is head.next:
                    return True
                head.next = head = head.next.next
        except:
            return False
    
