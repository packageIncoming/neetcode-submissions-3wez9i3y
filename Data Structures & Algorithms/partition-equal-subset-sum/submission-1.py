class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2

        def permute(curSum,i):
            nonlocal target
            if i == len(nums):
                if curSum == target:
                    return True
                else:
                    return False
            #with current
            withCur = permute(curSum+nums[i],i+1)
            #without current
            withoutCur = permute(curSum,i+1)
            return withCur or withoutCur
        return permute(0,0)