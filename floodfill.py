"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. 
You should perform a flood fill on the image starting from the pixel image[sr][sc].

"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        Return the image as-is if there is no color change (this helps avoid infinite loop in recursion)
        Return if we reach the edges, continue to fill otherwise        
        """
        
        m = len(image[:])
        n = len(image[0])
        if image[sr][sc] == newColor:
            return image
        if sr < 0 or sc < 0 or sr > m - 1 or sc > n - 1:
            return image
          
        prev = image[sr][sc]
        image[sr][sc] = newColor
        if sr > 0:
            if prev == image[sr-1][sc]:
                self.floodFill(image,sr-1,sc, newColor)
        if sc > 0:
            if prev == image[sr][sc-1]:
                self.floodFill(image,sr,sc-1, newColor)
        if sr < m-1:
            if prev == image[sr+1][sc]:
                self.floodFill(image,sr+1,sc, newColor)
        if sc < n-1:
            if prev == image[sr][sc+1]:
                self.floodFill(image,sr,sc+1, newColor)
        return image


"""
using collections.deque
from the top answer
"""

from typing import List
from collections import deque

class Solution_faster:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int
                  ) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        m = len(image)
        n = len(image[0])
        pre_color = image[sr][sc]
        image[sr][sc] = newColor
        q = deque([(sr, sc)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            i, j = q.popleft()
            for a, b in directions:
                x = i + a
                y = j + b
                if 0 <= x < m and 0 <= y < n and image[x][y] == pre_color:
                    image[x][y] = newColor
                    q.append((x, y))
        return image
