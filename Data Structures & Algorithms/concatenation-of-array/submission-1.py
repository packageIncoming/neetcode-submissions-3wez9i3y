class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_n = [0] * len(nums)*2
        for i in range(len(nums)*2):
            new_n[i] = nums[i%len(nums)]
        return new_n