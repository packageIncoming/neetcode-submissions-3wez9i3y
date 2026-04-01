class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curVal = nums[0]
        for num in nums[1:]:
            curVal = max(num,curVal+num)
            res = max(res,curVal)
        return res