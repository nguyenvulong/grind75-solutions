"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

Thanks: top answer and Nam_22 
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        if x is even: x and x/2 would have the same number of '1' bits
        if x is odd: x would have more '1' bits than x - 1 (count(x) = count(x-1) + 1)
        """
        ans = list()
        ans.append(0)
        for i in range(1,n+1):
            if i % 2 == 0:
                ans.append(ans[i//2])
            if i % 2 == 1:
                ans.append(ans[i-1] + 1)
        return ans
        
       
       
       
class Solution_top:
    def countBits(self, n: int) -> List[int]:
        """
        in this solution, the author handled odd and even cases nicely with 'i % 2'
        note that num_bits[i + 1] = num_bits[i] + 1 = num_bits[i//2] + 1
        """
        num_bits = [0] * (n + 1)
        num_bits[0] = 0
        for i in range(1, n + 1):
            num_bits[i] = i % 2 + num_bits[i // 2]
        return num_bits
