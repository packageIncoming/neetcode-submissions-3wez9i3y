class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            while l < len(nums) and nums[l] != val:
                l+=1
            #at this point we should be pointing to a non-desired value
            while r > l and  nums[r] == val:
                r-=1 
            # at this point r should reference a spot that we can 'throw away' this val
            if l >=r: break # crossed over check
            nums[l], nums[r] = nums[r],nums[l]
            l+=1
        return l