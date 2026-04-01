'''
The range would be between max(nums) and sum(nums)
How do you verify?: 
    - Iterate left to right, making a running sum
    - Whenever that sum = the value you're testing 

If sections(s) > k then it does not work
if sections(s) == k then it works
if sections(s) < k then it should also work(?)
'''
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def howManySectionsWithSum(s):
            curK = 0
            curSum = 0
            for i in range(len(nums)):
                if curSum + nums[i] <= s:
                    curSum+=nums[i]
                else:
                    curK+=1
                    curSum = nums[i]
            if curSum > 0:
                curK+=1
            return curK
        l,r = max(nums), sum(nums)
        highestSum = 0
        while l <=r:
            mid = (l+r)//2
            sections = howManySectionsWithSum(mid)
            if sections <= k:
                highestSum = mid
                r=mid-1
            else:
                # need to move up
                l=mid+1
                

        return highestSum