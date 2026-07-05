class MyQueue:

    def __init__(self):
        self.top = []
        self.bottom = []

    def push(self, x: int) -> None:
        self.bottom.append(x)

    def pop(self) -> int:
        if len(self.top) ==0:
            for i in range(len(self.bottom)):
                self.top.append(self.bottom.pop())
        return self.top.pop()

    def peek(self) -> int:
        if len(self.top)>0:
            return self.top[-1]
        else:
            return self.bottom[0]

    def empty(self) -> bool:
        return len(self.top)==0 and len(self.bottom)==0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()