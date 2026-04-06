'''
the minimum is going to be n[0] from the original unrotated array
in the rotated array,
n[0] is going to be the smallest of the large numbers
n[-1] is going to be the largest of the small numbers

at index i
if nums[i] > nums[-1]: we are in the right so we have to move up
otherwise move down

'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        lowest = -1
        while l<=r:
            mid  = (l+r)//2
            if nums[mid] > nums[-1]:
                l=mid+1
            else:
                lowest=mid
                r=mid-1

        return nums[lowest]