class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # memory optmized bottom-up solution
        dp = defaultdict(int)
        dp[0]=1 #1 way to sum to 0 using no elements
        for i in range(len(nums)):
            newRow = defaultdict(int)
            for cur_sum,cur_count in dp.items():
                newRow[cur_sum + nums[i]] += cur_count
                newRow[cur_sum - nums[i]] += cur_count
            dp=newRow
        return dp[target]
        memo = {}
        def dfs(i,curAmount):
            tag = (i,curAmount)
            if curAmount == target and i == len(nums):
                return 1
            if i >= len(nums):
                return 0
            if tag in memo:
                return memo[tag]
            # at any point we can either add or subtract the current value
            added = dfs(i+1,curAmount+nums[i])
            subtracted = dfs(i+1,curAmount-nums[i])
            memo[tag]=added + subtracted
            return memo[tag]
        
        return dfs(0,0)
