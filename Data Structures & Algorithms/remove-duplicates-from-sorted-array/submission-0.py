class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        ptr = 1
        while ptr < len(nums):
            while ptr < len(nums) and nums[ptr] == nums[ptr-1]:
                ptr+=1
            if ptr >= len(nums):break
            nums[k] = nums[ptr]
            ptr+=1
            k+=1

        return k