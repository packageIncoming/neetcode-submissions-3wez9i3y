class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #This avoids resizing since we already know the requisite length
        new_n = [0] * len(nums)*2
        for i in range(len(nums)*2):
            new_n[i] = nums[i%len(nums)]
        return new_n