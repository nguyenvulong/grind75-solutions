"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in string.ascii_lowercase:
            if s.count(c) != t.count(c):
                return False
        return True

     
"""
This approach below is more optimal
But make sure to check the lengths of both strings
""

class Solution_Faster:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        unique_char = set(s)
        for char in unique_char:
            if s.count(char) != t.count(char):
                return False

        return True
