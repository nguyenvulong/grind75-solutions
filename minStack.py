"""
Design a stack that supports push, pop, top, 
and retrieving the minimum element in constant time.


Thanks: https://leetcode.com/ksylvan
"""

class MinStack:
    """
    we use a tuple to store a pair of an element & min value
    `getMin` always returns the last element [-1]
    when `push` new element to the stack, make sure to check if that 
    element is the min value or not
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__a = []

    def push(self, x: int) -> None:
        m = x
        if self.__a:
            m = self.__a[-1][1]
            if m > x:
                m = x
        self.__a.append((x, m))

    def pop(self) -> None:
        self.__a.pop()
        
    def top(self) -> int:
        return self.__a[-1][0]

    def getMin(self) -> int:
        return self.__a[-1][1]
