# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.s = ""
        def dfs(node):
            if node is None:
                self.s +="N,"
                return
            self.s += f"{node.val},"
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(self.s)
        return self.s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.vals = data.split(",")[:-1]
        self.i=0
        def dfs():
            if self.i > len(self.vals) or self.vals[self.i] == "N":
                return
            node = TreeNode(int(self.vals[self.i]))
            self.i+=1
            node.left = dfs()
            self.i+=1
            node.right = dfs()
            return node
        return dfs()