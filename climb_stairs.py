"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?

Thanks: Top answers, Tushar Roy - Coding Made Simple, and the community
"""


class Solution_dp:
    def climbStairs(self, n: int) -> int:
        f = [1,2]
        for i in range(2,n):
            f.append(f[i-1]+f[i-2])
        return f[n-1]
      
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        classic Fibonaci series
        """
        a = b = 1
        for _ in range(0, n):
            a, b = b, a + b
        return a


class Solution_recursive:
    def climbStairs(self, n: int) -> int:
        """
        classic Fibonaci series
        """
        if n == 2:
            return 2
        if n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        
