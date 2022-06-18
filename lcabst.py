"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
Thanks: yash17129 (I reimplemented his c++ submission in python3), and top answer
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_recursion:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        if (root.val < p.val and root.val< q.val):
            return self.lowestCommonAncestor(root.right,p,q)
        if (root.val > p.val and root.val> q.val):
            return self.lowestCommonAncestor(root.left,p,q)
        return root
    

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            if ((p.val < curr.val) and (q.val > curr.val)) or \
               ((p.val > curr.val) and (q.val < curr.val)) or \
                (p.val == curr.val) or (q.val == curr.val):
                return curr
