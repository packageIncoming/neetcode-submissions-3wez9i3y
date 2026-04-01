class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # target for each subset is sum(nums)//k
        numsTotal = sum(nums) # o(n)
        target = numsTotal // k
        if k == 1: return True # just the array
        if (numsTotal % k != 0): return False # cannot evenly divide (integers only)

        usedMap = [0]*len(nums)
        nums.sort(reverse=True) # from largest to smallest

        def backtrack(i,curSum,curK):
            if curSum > target: return False # over the limit
            if curK == 0: return True # success case
            if curSum == target:
                return backtrack(0,0,curK-1)
            for j in range(i,len(nums)):
                if usedMap[j] == 1 or curSum+ nums[j] > target: continue # don't re-use OR don't use overflowing value
                if j > 0 and nums[j] == nums[j-1] and usedMap[j-1] == 0: continue # don't re-check
                # use
                usedMap[j]=1
                if backtrack(j+1,curSum+nums[j],curK):
                    return True
                # don't use
                usedMap[j]=0

                if curSum == 0:
                    return False
            return False
        return backtrack(0,0,k)