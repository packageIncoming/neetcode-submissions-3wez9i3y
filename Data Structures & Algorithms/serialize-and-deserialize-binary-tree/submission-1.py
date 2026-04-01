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
        self.cur_idx=0
        def dfs(node,idx):
            if node is None:
                return
            data_str = f"{node.val}:{idx}:{2*idx+1}:{2*idx+2},"
            self.s+= data_str
            dfs(node.left,2*idx+1)
            dfs(node.right,2*idx+2)
        dfs(root,0)
        return self.s
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_split = data.split(",")[:-1]
        # data = (node value):(node index):(node left index):(node right index)
        # 1. construct hashmap from bottom up
        hmap = {}
        for i in range(len(data_split)-1,-1,-1):
            node_val,node_idx,left_idx,right_idx = data_split[i].split(":")
            node = TreeNode(int(node_val))
            hmap[int(node_idx)] = node
            if int(left_idx) in hmap:
                node.left = hmap[int(left_idx)]
            if int(right_idx) in hmap:
                node.right = hmap[int(right_idx)]

        #print(data_split)
        return hmap[0] if len(hmap) > 0 else None