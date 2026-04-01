class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total %2!=0: return False
        memo = {}

        def find(remainder,i):
            nonlocal memo
            tag = (remainder,i)
            if remainder == 0 :
                 memo[tag] = True
                 return True
            if remainder <0 or i >= len(nums):
                memo[tag] =False
                return False
            if tag in memo:
                return memo[tag]
            # two possibilities, with or without current
            # with current
            withCur = find(remainder-nums[i],i+1)
            withoutCur = find(remainder,i+1)
            memo[tag] = withCur or withoutCur
            return memo[tag]
        return find(total//2,0)