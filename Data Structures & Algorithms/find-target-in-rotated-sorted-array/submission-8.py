'''
when the array gets rotated it effectively gets split into a lefthand and righthand side
[1,2,3,4,5,6] -> [3,4,5,6,1,2] [3,4,5,6] is one half and [1,2] is the other half

are there any special numbers?
-> elems[-1] is the biggest of the lefthand side
we don't know how big the lefthand side is (ie we don't know how many got rotated)


as a human, i would try to find the lefthand and righthand sides 
and then run binary search on whichever section the target would be in


step by step:
Input: nums = [3,4,5,6,1,2], target = 1



Output: 4



'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def find_lowest_idx(arr):
            l,r = 0, len(nums)-1
            l_idx = 0
            while l<=r:
                mid = (l+r)//2
                # if the middle is  greater than the rightmost then
                # it's in the right half
                # if the middle is less than the leftmost then
                # it's in the left half BUT we don't know if its the end
                # so just update the l_idx to mid and keep looking
                # to see if we can find anything smaller
                if arr[mid] > arr[-1]:
                    # gotta search higher
                    l=mid+1
                else:
                    # could be but we can keep looking
                    l_idx=mid
                    r=mid-1
            return l_idx

        def bsearch(arr,l,r,target):
            while l<=r:
                mid = (l+r)//2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    r=mid-1
                else:
                    l=mid+1
            return -1

        lowest_idx = find_lowest_idx(nums)
        if nums[lowest_idx]<=target<=nums[-1]:        
            return bsearch(nums,lowest_idx,len(nums)-1,target)
        else:
            return bsearch(nums,0,lowest_idx-1,target)


        