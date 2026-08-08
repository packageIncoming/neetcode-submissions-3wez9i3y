'''

HICS

How would I do this?:

I get the feeling this is something to do with prefix/suffix arrays
[1,3,5]

THERE IS REPEATED WORK HERE

summing from [1,3,] to [1,3,5] has repeated work so there's no point in re-summing

The brute force solution would be to get a sum starting from every point

So we're getting TLE 

The issue is that there's repeated work 
let's build an array
if you have
[1] then the only subarray sum is [1]
[1,2] you have [1,3] 
[1,2,3] you have [1,3,6] 
if you go from right to left then
[3] -> [3]
[2,3] -> [5,3]

[1,3,5]
[1,4,9]
[5,8] don't re-include the first
but then you also have all the individuals

[1,2,3,4,5,6,7]
[1,3,6,10,15,21,28]
[7,13,18,22,25,27]

the missing sections are in the middle
YOU HAVE TO DO MULTIPLE PASSES
[1,2,3,4,5,6,7]

'''


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        MOD = (10**9)+7

        curSum = 0
        curNumOdd = 0
        curNumEven = 0
        for i in range(len(arr)):
            curSum+= arr[i]
            if curSum %2 ==0:
                curNumEven+=1
                res+= curNumOdd
            else:
                curNumOdd+=1
                res += 1 + curNumEven

        return res % MOD
        