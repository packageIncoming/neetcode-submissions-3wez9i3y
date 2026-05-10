# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # left = 2i
        # right = 2i+1
        res = []
        def dfs(i,node):
            if not node: return
            nonlocal res
            res.append(f"{i}/{node.val}")
            dfs(2*i,node.left)
            dfs(2*i+1,node.right)
        dfs(1,root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0: return None
        pairs = data.split(',')
        nodedict = {}
        for i in range(len(pairs)-1,-1,-1):
            position,value = pairs[i].split('/')
            position=int(position)
            value = int(value)
            node = TreeNode(val=value)
            nodedict[position] = node
            if 2*position in nodedict:
                node.left = nodedict[2*position]
            if 2*position+1 in nodedict:
                node.right = nodedict[2*position+1]
        return nodedict.get(1,None)
            
