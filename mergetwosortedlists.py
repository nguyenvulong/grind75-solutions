"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Thanks: Maelstrom's answer from https://stackoverflow.com/questions/31553576/converting-a-list-to-a-linked-list
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output = []
        while True:
            if list1 == None and list2 == None:
                break
            
            if list2 == None or (list1 != None and list1.val < list2.val):
                output.append(list1.val)
                list1 = list1.next
            elif list1 == None or (list2 != None and list1.val >= list2.val):
                output.append(list2.val)
                list2 = list2.next

                
        return self.list_to_link(output)
    
    def list_to_link(self, lst):
        """Takes a Python list and returns a Link with the same elements.
        """
        if len(lst) == 0:
            return None
        if len(lst) == 1:
            return ListNode(lst[0])
        return ListNode(lst[0], self.list_to_link(lst[1:]))  # <<<< RECURSIVE
      
      
class Solution_better:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        new_head = ListNode()
        prev = new_head
        
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        
        if list1:
            prev.next = list1
        if list2:
            prev.next = list2
            
        return new_head.next
        
