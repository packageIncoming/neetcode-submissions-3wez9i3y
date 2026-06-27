'''

if subarray then must be contiguous & non-empty

[2,-1,1,2] k=2
output = 4

you're not returning the actual arrays, you're returning the # that sum to k

entries can be negative so can't just reset (kadane)

also cannot sort since that breaks the ordering


'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        pmap={}
        pmap[0]=1

        curSum=0
        res=0

        for i in range(len(nums)):
            curSum+=nums[i]
            diff = curSum-k
            res+= pmap.get(diff,0)
            pmap[curSum] = pmap.get(curSum,0)+1
            


        return res
        