

class StockSpanner:

    def __init__(self):
        self.nums=[] # elements are tuples (price,span)

    def next(self, price: int) -> int:
        # monotonically decreasing stack
        cnt=1
        while self.nums and self.nums[-1][0] <= price: # while old price <= cur price
            cnt+=self.nums[-1][1] # add to streak
            self.nums.pop()
        self.nums.append((price,cnt))
        return cnt


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)