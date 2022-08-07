"""
Given two binary strings a and b, return their sum as a binary string.
Thanks: top answer
"""

class Solution:
    """
    Python3 support converting from binary str to int
    int(number,2)
    """
    def addBinary(self, a: str, b: str) -> str:
        def to_int(a: str):
            i = -1
            sum = 0
            while True:
                sum = sum + 2**(abs(i)-1)*int(a[i])
                i = i - 1
                if abs(i) > len(a):
                    break
            return sum
        if a == "0" or b == "0":
            return max(a,b)
        #print(to_int(a),to_int(b))
        sumab = to_int(a) + to_int(b)
        return str(bin(sumab)[2:])
      
      
class Solution_top:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]
