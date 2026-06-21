'''

implement a hashing function is probably the more learning intensive thing here


'''



class MyHashSet:

    def __init__(self):
        self.buckets=[[] for i in range(50)]

        

    def add(self, key: int) -> None:
        bucket = key % 50
        for i in range(len(self.buckets[bucket])):
            if self.buckets[bucket][i] == key:
                return
        self.buckets[bucket].append(key)

        

    def remove(self, key: int) -> None:
        idx = key % 50
        bucket = self.buckets[idx]
        try:
            i = bucket.index(key)
            if i != -1:
                bucket.pop(i)
        except:
            pass

        

    def contains(self, key: int) -> bool:
        bidx = key % 50
        bucket = self.buckets[bidx]
        for i in range(len(bucket)):
            if bucket[i] == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

