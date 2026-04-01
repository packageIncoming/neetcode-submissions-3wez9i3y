from collections import deque
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        xor_tot = 0
        for num in nums:
            xor_tot = xor_tot | num

        return xor_tot * 2**(len(nums)-1)