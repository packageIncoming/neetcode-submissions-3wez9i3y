class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(cur,i,s):
            if s > target:
                return # overflow
            if s == target:
                res.append(cur.copy())
                return
            if i >= len(nums): 
                return # didn't equal target but ran out of numbers
            
            # at each step we can either include the current number OR move to the next
            cur.append(nums[i])
            dfs(cur,i,s+nums[i]) # DONT MOVE ON since we could re-use
            cur.pop()
            dfs(cur,i+1,s) # MOVE ON 
        
        dfs([],0,0)

        return res