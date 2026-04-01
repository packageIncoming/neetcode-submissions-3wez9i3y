'''
Whenever you try a house at index i, indices i-1 and i+1 must be skipped 

'''
class Solution:


    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def robHelper(arr):
            self.memo = {}
            def track(i):
                if i >= len(arr):
                    return 0
                if i not in self.memo:
                    self.memo[i] = max(arr[i] + track(i+2),track(i+1))
                return self.memo[i] 
            return track(0)    
        withFirst = nums[:-1]
        withSecond = nums[1:]

        return max(robHelper(withFirst),robHelper(withSecond))