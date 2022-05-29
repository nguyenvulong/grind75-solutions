"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Thanks: fdhwas
"""


class Solution:
    def isValid(self, s: str) -> bool:
        LR = {'{':'}', '(':')','[':']'}
        
        stack = list()
        for i in s:
            if i in LR:
                stack.append(i)
            elif  stack == [] or i != LR[stack.pop()]:
                return False
        if len(stack) == 0:
            return True
