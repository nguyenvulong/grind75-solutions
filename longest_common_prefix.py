"""
Write a function to find the longest common prefix string amongst an array of strings.
Thanks: top answer
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        only need to find the longtest common string of the shortest one and another
        """
        if not strs: return ''
        s1 = min(strs)
        s2 = max(strs)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i] #stop until hit the split index
        return s1
                
