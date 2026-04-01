class MyHashSet:

    def __init__(self):
        self.keys=[]

    def add(self, key: int) -> None:
        for num in self.keys:
            if num == key:
                return
        self.keys.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                for j in range(i,len(self.keys)-1):
                    self.keys[j] = self.keys[j+1]
                self.keys.pop()
                return

    def contains(self, key: int) -> bool:
        for num in self.keys:
            if num==key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)