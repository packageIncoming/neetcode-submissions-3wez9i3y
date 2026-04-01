class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1: return 0 if nums[0] == target else -1
        # First find the cut of the array, then search within the range the target would be in
        l, r = 0, len(nums)-1
        minValue = nums[0]
        cutIdx = 0
        while l <= r:
            mid = (l+r)//2
            #Update cut index if mid is smaller than minValue
            if nums[mid] < minValue:
                cutIdx = mid
                minValue = nums[mid]

            if nums[mid] > nums[r]:
                l=mid+1
            else:
                r=mid-1
        # Update ranges based on cut point
        l,r = 0, len(nums)-1
        if target >= nums[0] and cutIdx > 0 and target <= nums[cutIdx-1]:
            r=cutIdx-1
        else:
            l=cutIdx
        # Now perform binary search on the updated ranges
        print(target,l,r,nums[l:r+1])
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r=mid-1
            else:
                l=mid+1
        

        return -1 