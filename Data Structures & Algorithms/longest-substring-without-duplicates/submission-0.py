class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #solution 1 (optimal solution):
        # two pointers, expand right until rule is broken, then shrink
        #from left, repeat until right pointer has reached the end of s
        r_ptr =0
        l_ptr = 0
        max_len = 0
        cur_set = set()
        while r_ptr < len(s):
            while s[r_ptr] in cur_set:
                cur_set.remove(s[l_ptr])
                l_ptr+=1
            cur_set.add(s[r_ptr])
            r_ptr+=1
            max_len = max(max_len, (r_ptr - l_ptr))
        return max_len