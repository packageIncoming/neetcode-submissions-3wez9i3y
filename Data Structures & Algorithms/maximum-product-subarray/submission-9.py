class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP,minP = 1,1
        res = nums[0]
        for num in nums:

            temp = maxP
            maxP = max(maxP * num,minP*num,num)
            minP = min(temp*num,minP*num,num)
            res = max(maxP,res)


        return res