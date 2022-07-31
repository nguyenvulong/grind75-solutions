"""
Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 

There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Thanks: top answer
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        """
          ret: integer
          from right to left, if a number is smaller than the one next to it
          then it's a subtraction
        """
        symval = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        c = 0
        res = 0
        while c < len(s):
            if c == len(s) - 1:
                res = res + symval[s[c]]
                break
                
            first = symval[s[c]]
            second = symval[s[c+1]]
            if first < second:
                res = res - first
            else:
                res = res + first
            #print(c, res)
            c = c + 1
            
        return res

class Solution_top:
    def romanToInt(self, s: str) -> int:
        """
        expand the roman number by replacement then add all up
        """
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
        
