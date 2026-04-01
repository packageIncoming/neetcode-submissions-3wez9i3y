class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        minVal = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            minVal = min(minVal, nums[mid])
            if nums[mid] >= nums[r]:
                l=mid+1
            else:
                r=mid-1                
        print(mid)
        return minVal

