"""
Given a string s which consists of lowercase or uppercase letters, 
return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Thanks: top answer
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        3 cases happen when counting `i`: even, odd, and 1
        we can make the three cases into one:
        
        if s.count(i) != 1:
            cnt = cnt + s.count(i) - (s.count(i) % 2)
            odd = odd + (s.count(i) % 2)
            
        below is my original solution
        """
        if len(set(s)) == 1:
            return len(s)
        cnt = 0
        odd = 0
        for i in set(s):
            print(i, s.count(i))
            if s.count(i) % 2 == 0:
                cnt = cnt + s.count(i)
            elif s.count(i) != 1:
                cnt = cnt + s.count(i) - 1
                odd = odd + 1
            else:
                odd = odd + 1
        cnt = cnt + min(odd,1)
        return cnt
  
  
class Solution_top:
    def longestPalindrome(self, s: str) -> int:
        odd = ret = 0
        
        for ch in set(s):
            ct = s.count(ch)
            ret += ct - (ct % 2)
            odd |= ct % 2
        
        return ret + odd
