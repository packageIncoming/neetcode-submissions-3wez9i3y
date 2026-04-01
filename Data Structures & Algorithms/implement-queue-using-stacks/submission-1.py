class MyQueue:

    def __init__(self):
        self.size=0
        self.stack=[]

    def push(self, x: int) -> None:
        self.size+=1
        self.stack.append(x)

    def pop(self) -> int:
        temp = []
        for i in range(self.size-1):
            temp.append(self.stack.pop())
        val = self.stack[-1]
        for i in range(len(temp)):
            self.stack.append(temp.pop())
        self.size-=1
        return val

    def peek(self) -> int:
        temp = []
        for i in range(self.size-1):
            temp.append(self.stack.pop())
        val = self.stack[-1]
        temp.append(self.stack.pop())
        for i in range(len(temp)):
            self.stack.append(temp.pop())
        return val

    def empty(self) -> bool:
        return self.size==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()