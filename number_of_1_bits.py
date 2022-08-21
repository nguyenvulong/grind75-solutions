"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
Thanks: top answers and DBabichev https://leetcode.com/problems/number-of-1-bits/discuss/1044775/Python-n-and-(n-1)-trick-%2B-even-faster-explained
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        def count1(n):
            return bin(n).count('1')
        
        def count2(i):
            "Recursion"
            if i == 0:
                return 0
            if i == 1:
                return 1
            print("i = {}".format(i))
            if i % 2 == 0:
                return count(i//2)
            else:
                return count(i//2) + 1
    
        def count3(i):
            "DP but time limit exceeded"
            track = []
            track.append(0)
            track.append(1)
            #print("i = {}".format(i))
            for j in range(2,i+1):
                #print("j = {}".format(j))
                if j % 2 == 0:
                    track.append(track[j//2])
                else:
                    track.append(track[j//2] + 1)
            #print(track)
            return track[i]
          
        def count(n):
            """
            n & n-1 will remove the right most bit
            keep doing so until n = 0
            """
            ans = 0
            while n:
                n &= (n-1)
                ans += 1
            return ans
        return count(n)
