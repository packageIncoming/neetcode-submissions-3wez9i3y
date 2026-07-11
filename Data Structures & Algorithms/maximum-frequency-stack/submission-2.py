'''
idea
frequency hash map + buckets of frequencies

keep a frequency of each item with a defaultdict
then have another hashmap of int frequency: list[int] value

'''

class FreqStack:

    def __init__(self):
        self.freqs = {}
        self.buckets = defaultdict(list)
        self.maxFreq=0
        

    def push(self, val: int) -> None:
        prev = self.freqs.get(val,0)
        self.freqs[val] = prev+1
        self.buckets[prev+1].append(val)
        self.maxFreq = max(self.maxFreq,prev+1)

    def pop(self) -> int:
        topBucket = self.buckets[self.maxFreq]
        val = topBucket.pop()
        self.freqs[val]-=1
        if len(topBucket)==0:
            self.maxFreq-=1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()