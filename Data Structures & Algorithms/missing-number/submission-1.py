class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        e_sum= sum(x for x in range(n+1))
        s = sum(num for num in nums)

        return e_sum - s