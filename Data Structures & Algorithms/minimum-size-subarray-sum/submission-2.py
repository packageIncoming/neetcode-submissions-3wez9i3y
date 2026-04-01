class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curLen = float('inf')

        curSum = 0
        l = 0
        for i in range(len(nums)):
            curSum+=nums[i]
            while curSum - nums[l] >= target:
                curSum -= nums[l]
                l+=1
                curLen = min(curLen,i-l+1)
            if curSum >= target:
                curLen = min(curLen,i-l+1)



        if curLen == float('inf'): 
            return 0
        else:
            return curLen