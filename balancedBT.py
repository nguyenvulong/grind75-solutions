"""
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

thanks: top answer
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            
            left, right = dfs(root.left), dfs(root.right)
            
            if abs(left-right) > 1:
                return -1
            if left == -1 or right == -1:
                return -1
            return max(left,right) + 1
            
        if dfs(root) == -1:
            return False
        return True
      
class Solution_mine:
    def height(root):
        # base condition when binary tree is empty
        if root is None:
            return 0
        return max(height(root.left), height(root.right)) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if abs(height(root.left) - height(root.right)) > 1:
            return False
        L = self.isBalanced(root.left)
        R = self.isBalanced(root.right)
        if L and R:
            return True
        return False
