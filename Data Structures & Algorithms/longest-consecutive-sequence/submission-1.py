class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = {}
        set_nums = set(nums)
        longest = 0

        for s in set_nums:
            if s-1 not in set_nums:
                cur_len = 0
                cur = s
                while cur in set_nums:
                    cur_len +=1
                    cur = cur+1 
                longest = max(longest,cur_len)
            

        return longest
        