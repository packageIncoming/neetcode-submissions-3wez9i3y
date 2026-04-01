'''

arr[-1] will be the highest value of the small range
arr[n-1] will be the max value  in the array

idea:
    is target <= arr[-1]?
    If it is that means it is between arr[n] and arr[-1]
    If not then that means it is between arr[0] and arr[n-1]

    Figure out which section target is in, then binary search to find pivot
    then find target within that section

'''

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1

        while l <=r:
            mid = (l+r)//2
            # if nums[l]==nums[mid]==nums[r], indecisive, just move inwards
            if nums[mid] == target:
                return True

            if nums[mid] > nums[l]:
                # we are currently in the high portion

                if nums[l] <= target < nums[mid]:
                    # but the target is smaller than mid
                    r=mid-1
                else:
                    # but the target is greater than the mid
                    l=mid+1
            elif nums[l] > nums[mid]:
                # we are currently in the low portion

                if nums[mid] < target <= nums[r]:
                    # move higher
                    l=mid+1
                else:
                    # move lower
                    r=mid-1
            else:
                l+=1

        return False


