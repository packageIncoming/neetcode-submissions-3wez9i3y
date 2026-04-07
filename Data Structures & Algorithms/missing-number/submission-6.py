class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expected=int(n*(n+1)/2)
        res = 0
        for num in nums:
            res+=num
        return expected-res