"""
Given two strings s and t, return true if they are equal when both
are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
Thanks: yuzhoujr
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
            
        
class Solution_stack:
    def backspaceCompare(self, S, T):
        l1 = self.stack(S, [])
        l2 = self.stack(T, [])
        return l1 == l2
        
    
    def stack(self, S, stack):
        """
        use stack to `pop` when "#" is found
        """
        for char in S:
            if char is not "#":
                stack.append(char)
            else:
                if not stack:
                    continue
                stack.pop()
        return stack
