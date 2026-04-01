'''
* New position is (index+k)% len(arr)

O(n) solution would be to instantiate new empty array then fill accordingly
then replace values in nums based on that 


'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        newVals = [0]*len(nums)
        for i in range(len(nums)):
            newVals[(i+k)%len(nums)] = nums[i]
        for i in range(len(newVals)):
            nums[i] = newVals[i]
