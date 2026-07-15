'''
2 pointers obviously

[1,1,2,3,4]

since it wants the elements to be at the front maybe start from the front

need some way to find a duplicate & a way to move a non-duplicate into that spot


'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        

        l=1
        r=l

        while r< len(nums):
            while r<len(nums) and nums[r] == nums[r-1]:
                r+=1
            if r  == len(nums): break
            nums[l]= nums[r]
            l+=1
            r+=1
            

        return l