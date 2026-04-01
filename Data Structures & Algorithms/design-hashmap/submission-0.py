class MyHashMap:

    def __init__(self):
        # array of 2D arrays
        # this ends up with O(n) on pretty much all operations , maybe easier with hashset but problem asks to not use hash table libs

        self.pairs = []


    def put(self, key: int, value: int) -> None:
        firstEmpty = None
        for pair in self.pairs:
            if pair[0] == -1 and pair[1] == -1 and firstEmpty is None:
                firstEmpty= pair
            if pair[0] == key:
                pair[1] = value # update existing 
        if firstEmpty:
            firstEmpty[0] = key
            firstEmpty[1] = value
        else:
            self.pairs.append([key,value])

    def get(self, key: int) -> int:
        for pair in self.pairs:
            if pair[0] == key and pair[1] != -1:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        for pair in self.pairs:
            if pair[0] == key:
                pair[0] = -1
                pair[1] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)