class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #already sorted
        if target <= nums[0]: return 0
        if target > nums[-1]: return len(nums)
        l,r = 0,len(nums)-1
        while l <=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid # exact same spot
            elif nums[mid]> target:
                if target > nums[mid-1]:
                    return mid
                else:
                    r=mid-1
            elif nums[mid] < target:
                l=mid+1
        return (l+r)//2