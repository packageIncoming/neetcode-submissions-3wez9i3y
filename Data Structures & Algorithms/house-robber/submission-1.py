class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        def getHighestProfitStartingFrom(index):
            if index >= len(nums):
                return 0 # OOB
            # try robbing the current(cannot rob next)
            # don't rob the current (can rob next)
            if index in self.memo:
                return self.memo[index]
            self.memo[index] = max(nums[index] + getHighestProfitStartingFrom(index+2),getHighestProfitStartingFrom(index+1))
            return self.memo[index]
        
        return getHighestProfitStartingFrom(0)