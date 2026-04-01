class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = []
        def dfs(i,path):
            if i == len(nums):
                subs.append(path)
                return
            dfs(i+1,path.copy())
            p2 = path.copy()
            p2.append(nums[i])
            dfs(i+1,p2)
        dfs(0,[])
        return subs