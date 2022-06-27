"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Thanks: top-1 answer for mutated string answer, 
        top-2 for the hint of using "set" to make my solution run faster
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for s in set(ransomNote):
            if ransomNote.count(s) > magazine.count(s):
                return False
        return True

class Solution_mutation:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for rc in ransomNote:
            if rc in magazine:
                i = magazine.index(rc)
                magazine = magazine[:i:] + magazine[i+1:]
            else:
                return False
        return True
