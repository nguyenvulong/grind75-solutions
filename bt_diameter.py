"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
Thanks: https://leetcode.com/{tree_guy,gubd}
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # assume that diameter = 0
        # ans is a `nonlocal` variable
        ans = 0 
        def height(node):
            # return -1 for empty node, we compensate that later if it's not None
            nonlocal ans
            if not node:
                return -1 
            left, right = height(node.left), height(node.right)
            ans = max(ans, 2 + left + right)
            
            # if node is not None, height+=1
            return 1 + max(left,right)
        
        # start counting the height of the tree
        # and at the same time, measure it diameter
        height(root)
        return ans
            
            
        
