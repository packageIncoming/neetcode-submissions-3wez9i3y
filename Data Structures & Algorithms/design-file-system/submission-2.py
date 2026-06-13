
'''
Off the rip this is literally just a Trie

The root node is '/' or '' but asking or creating the root should
return false or -1

Basically you'd take in the value, split by '/' then either
    If you're creating, traverse as much as possible
        and then add
    If you're getting, then traverse until you reach the end 




'''
class TrieNode:
    def __init__(self):
        self.val=None
        self.neighbors = {}
class FileSystem:



    def __init__(self):
        self.root = TrieNode()
        self.root.val = -1

        

    def createPath(self, path: str, value: int) -> bool:
        if path == '' or path == '/': return False
        parts = path.split('/')[1:]
        cur_node = self.root
        for i in range(len(parts)-1): # will stop at the parent before last value
            piece = parts[i]
            if piece not in cur_node.neighbors:
                return False # parent does not exist
            else:
                cur_node = cur_node.neighbors[piece]
        
        if parts[-1] in cur_node.neighbors:
            return False # already exists
        else:
            new_node = TrieNode()
            new_node.val = value
            cur_node.neighbors[parts[-1]] = new_node
            return True

    def get(self, path: str) -> int:
        if path == '' or path == '/': return -1
        parts = path.split('/')[1:]
        cur_node = self.root
        for i in range(len(parts)): # will stop at the node
            piece = parts[i]
            if piece not in cur_node.neighbors:
                return -1 # parent does not exist
            else:
                cur_node = cur_node.neighbors[piece]
        return cur_node.val
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
