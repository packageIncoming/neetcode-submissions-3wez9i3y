class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=0
        n= len(nums)
        expectedSum = n*(n+1)/2
        realSum=0
        zeroFound=False
        for num in nums:
            if num ==0:
                zeroFound = True
            realSum+=num
        if zeroFound is False:
            return 0
        else:
            return int(expectedSum-realSum)