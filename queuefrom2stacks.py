"""
Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
Thanks: top answer
"""

class MyQueue:

    def __init__(self):
        self.incoming = []
        self.outgoing = []

    def push(self, x: int) -> None:
        self.incoming.append(x)
        

    def pop(self) -> int:
        if self.outgoing:
            return self.outgoing.pop()
        while self.incoming:
            self.outgoing.append(self.incoming.pop())
        return self.outgoing.pop()

    def peek(self) -> int:
        if self.outgoing:
            return self.outgoing[-1]
        while self.incoming:
            self.outgoing.append(self.incoming.pop())
        return self.outgoing[-1]

    def empty(self) -> bool:
        return len(self.incoming) == 0 and len(self.outgoing) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
