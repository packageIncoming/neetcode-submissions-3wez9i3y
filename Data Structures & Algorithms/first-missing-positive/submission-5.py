class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # brute force O(N) space solution:
        lowest,highest = nums[0],nums[0]
        found = set()
        for num in nums:
            lowest = min(lowest,num)
            highest = max(highest,num)
            found.add(num)
        for i in range(1,highest+2):
            if i not in found:
                return i
        return 1