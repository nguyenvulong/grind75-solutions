"""
Given two strings s and t, return true if they are equal when both
are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def result(s) -> str:
            """
            from left to right, remove a character if the current one is "#"
            add it to the result string if it's not "#"
            """
            res = ""
            for i in s:
                if i == "#":
                    if len(res) > 0:
                        res = res[:-1]
                else:
                    res = res + i
            return res
        return result(s) == result(t)
            
        
