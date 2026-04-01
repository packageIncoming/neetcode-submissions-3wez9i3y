class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_n = []
        for i in range(len(nums)*2):
            new_n.append(nums[i%len(nums)])
        return new_n