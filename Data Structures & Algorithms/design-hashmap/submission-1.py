'''
binary tree implementation
whenever removed just set value to -1 since value <=0

'''

class Node():
    def __init__(self):
        self.value=None
        self.key=None

        self.left=None
        self.right=None

class MyHashMap:

    def __init__(self):
        self.root = Node()
        self.root.key=-1
        self.root.value=-1
        

    def put(self, key: int, value: int) -> None:
        prev=None
        cur=self.root
        while cur:
            if cur.key== key:
                cur.value =value
                return
            else:
                prev=cur
                if key > cur.key:
                    cur=cur.right
                else:
                    cur=cur.left
        new_node = Node()
        new_node.value = value
        new_node.key = key

        if new_node.key > prev.key:
            prev.right=new_node
        else:
            prev.left=new_node
        

    def get(self, key: int) -> int:
        cur=self.root
        while cur:
            if cur.key== key:
                return cur.value
            else:
                if key > cur.key:
                    cur=cur.right
                else:
                    cur=cur.left
        return -1
        

    def remove(self, key: int) -> None:
        cur=self.root
        while cur:
            if cur.key== key:
                cur.value = -1
                return
            else:
                if key > cur.key:
                    cur=cur.right
                else:
                    cur=cur.left
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)