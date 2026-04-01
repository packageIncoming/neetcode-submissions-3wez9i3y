class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # brute force solution: find the maximum product starting from any index and expanding left
        maxP = nums[0]
        for i in range(len(nums)):
            curProd = nums[i]
            maxP = max(maxP,curProd)
            for j in range(i+1,len(nums)):
                curProd *= nums[j]
                maxP = max(maxP,curProd)
        return maxP