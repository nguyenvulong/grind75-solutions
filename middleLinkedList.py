"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node

Thanks: top answer(s)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        slow fast approach
        fast speed = 2, slow speed = 1
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        

    def middleNode2(self, head: ListNode) -> ListNode:
        """
        measure linked list length, find the middle node's index
        loop one more time to find that node
        """
        x = head
        result = head
        count = 1
        
        while x.next != None:
            x = x.next
            count += 1

        mid = int(count / 2) + 1
        
        count = 1
        while count != mid:
            result = result.next
            count += 1
            
        return result
