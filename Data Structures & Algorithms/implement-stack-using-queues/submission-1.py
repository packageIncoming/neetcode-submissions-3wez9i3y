class MyStack:

    def __init__(self):
        self.q = collections.deque()

        self.size = 0


    def push(self, x: int) -> None:
        self.q.append(x)
        self.size+=1


    def pop(self) -> int:
        temp=collections.deque()

        for i in range(self.size-1):
            temp.append(self.q.popleft())

        val = self.q.popleft()
        self.size-=1

        for i in range(len(temp)):
            self.q.append(temp.popleft())

        return val

    def top(self) -> int:
        temp=collections.deque()

        for i in range(self.size-1):
            temp.append(self.q.popleft())

        top = self.q.popleft()
        temp.append(top)

        for i in range(len(temp)):
            self.q.append(temp.popleft())

        return top

    def empty(self) -> bool:
        return self.size==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()