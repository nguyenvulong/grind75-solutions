"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Thanks: yuan0209, StefanPochman
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def compareNode(p,q) ->bool:
            # print("p = {}, q = {}".format(p,q))
            # next time do not name variables p & q, myopic
            if p == q == None:
                return True
           
            if p != None and q != None:
                if p.val == q.val:
                    return compareNode(p.left,q.left) and compareNode(p.right,q.right)
                else:
                    return False
            return False
        return compareNode(p,q)
      
      
      
    def isSameTree_is(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q # check if they refer to the same object or not


    def isSameTree_tupleify(self, p, q):
        def t(n):
            return n and (n.val, t(n.left), t(n.right))
        return t(p) == t(q)
