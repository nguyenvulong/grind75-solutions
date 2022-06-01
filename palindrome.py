"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Thanks: 2 top answers
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alpha = "".join(filter(str.isalnum, s)).lower()
        j_index = len(s_alpha) - 1
        for i in range(len(s_alpha) // 2):
            if(s_alpha[i] != s_alpha[j_index]):
                print(f"fault reached, i: {i}, j: {j_index} ")
                return False
            j_index -= 1
        return True
      
      
class Solution_shorter:
    def isPalindrome(self, s: str) -> bool:
        s = ' '.join(filter(str.isalnum,s))
        s=s.lower()
        if s[::-1] == s:
            return True
