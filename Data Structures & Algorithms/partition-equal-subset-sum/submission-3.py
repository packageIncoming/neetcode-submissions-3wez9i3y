class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        memo = {target:True}
        def permute(curSum,i):
            nonlocal target

            if curSum in memo:
                return memo[curSum]
            if curSum > target:
                memo[curSum] = False
                return False
            
            if i == len(nums):
                if curSum == target:
                    return True
                else:
                    return False
            #with current
            memo[curSum+nums[i]] = permute(curSum+nums[i],i+1)
            withCur = memo[curSum+nums[i]]
            #without current
            memo[curSum] = permute(curSum,i+1)
            withoutCur = memo[curSum]
            return withCur or withoutCur
        return permute(0,0)