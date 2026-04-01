class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = {}
        # O(n)
        set_nums = set(nums)
        starts = set(n for n in set_nums if n-1 not in set_nums)
        longest = 0

        for s in starts:
            cur_len = 0
            cur = s
            while cur in set_nums:
                cur_len +=1
                cur = cur+1 
            longest = max(longest,cur_len)
            

        return longest
        