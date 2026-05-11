class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = nums[0]

        for i in range(1,len(nums)):
            curSum = max(curSum+nums[i],nums[i])
            maxSum = max(maxSum,curSum)


        return maxSum