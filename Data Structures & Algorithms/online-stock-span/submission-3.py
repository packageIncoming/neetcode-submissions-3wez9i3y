class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        v = 1
        while self.stack and self.stack[-1][0] <= price:
            r = self.stack.pop()
            v+= r[1]
        self.stack.append((price,v))
        return v


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)