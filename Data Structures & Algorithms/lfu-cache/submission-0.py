'''
it looks like the answer MUST have a use_counter for each key
get and put must both run in O(1), so there cannot be traversals or anything like that
so the least frequently used must in some sense be kept track of,
maybe with a pointer or some other variable


brute force solution with O(n) time on get and put:
    keep a hashmap of hash[key] = [count,value,lastUse]
    on get(), check if a value exists and return it if so (-1 if not)
    on put(), check if capacity full, if so then delete LFU (min count)
        and then add the new value
'''

# BRUTE FORCE SOLUTION:
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.curOperation=0
        self.cache = {}


    def get(self, key: int) -> int:
        self.curOperation+=1
        if key in self.cache:
            self.cache[key][0]+=1
            self.cache[key][2] = self.curOperation
            return self.cache[key][1]
        else:
            return -1

    def remove_lfu(self):
        if len(self.cache) == 0: return
        keys = list(self.cache.keys())
        lfu = keys[0]
        for key in keys:
            if self.cache[key][0] < self.cache[lfu][0]:
                lfu = key
            elif self.cache[key][0] == self.cache[lfu][0] and self.cache[key][2] < self.cache[key][2]:
                lfu = key
        if lfu: 
            del self.cache[lfu]
        

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity:
            self.remove_lfu()
        self.curOperation+=1
        self.cache[key] = [1,value,self.curOperation]


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)