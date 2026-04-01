class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1: return 0
        s = set()
        lowest = nums[0]
        highest = nums[0]
        for val in nums:
            if val not in s:
                s.add(val)
            lowest = min(lowest,val)
            highest = max(highest,val)
        cur_streak = 0
        longest_streak  =0
        print(s)
        while len(s) > 0 and lowest <= highest:
            if lowest in s:
                cur_streak+=1
                s.remove(lowest)
            else:
                cur_streak = 0
            longest_streak  =max(longest_streak,cur_streak)
            lowest+=1
        
        return longest_streak