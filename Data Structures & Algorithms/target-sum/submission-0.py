class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i,curAmount):
            if curAmount == target and i == len(nums):
                return 1
            if i >= len(nums):
                return 0
            # at any point we can either add or subtract the current value
            added = dfs(i+1,curAmount+nums[i])
            subtracted = dfs(i+1,curAmount-nums[i])
            return added + subtracted
        return dfs(0,0)
