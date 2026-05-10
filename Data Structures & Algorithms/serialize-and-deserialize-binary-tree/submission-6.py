# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("#")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0: return None
        vals = data.split(',')
        self.idx=0
        def dfs():
            if vals[self.idx]=='#':
                return None
            node = TreeNode(val=int(vals[self.idx]))
            self.idx+=1
            node.left = dfs()
            self.idx+=1
            node.right = dfs()
            return node
        return dfs()

            
