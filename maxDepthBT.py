"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf node
Thanks: top answer & discussion
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepthDFS(self, root: Optional[TreeNode]) -> int:
        def dfs(root) -> int: 
            if not root:
                return 0
            return max(dfs(root.left), dfs(root.right)) + 1
        return dfs(root)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(root) -> int:
            if root == None: return 0
            res = 1
            queue = [(root,1)]
            while queue:                    
                root, res = queue.pop(0)
                if root.left != None:
                    queue.append((root.left, res+1))
                if root.right != None:
                    queue.append((root.right, res+1))
            return res
        return bfs(root)
