class StockSpanner:

    def __init__(self):
        self.nums=[]

    def next(self, price: int) -> int:
        # brute force o(N) solution, just count backwards
        count=0
        self.nums.append(price)
        for i in range(len(self.nums)-1,-1,-1):
            if self.nums[i] <=price:
                count+=1
            else:
                break
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)