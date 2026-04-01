class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # super simple approach O(n) time and space
        s = set()
        for i in range(len(nums)):
            if nums[i] in s: return nums[i]
            s.add(nums[i])