
'''
if you have an array of numbers of length n, the highest that the first missing positive
can be is n+1

[1]->2
[1,2]->3
[1,2,3]->4

And of course the lowest positive integer is 1 

Cycle sort makes SO much more sense for this

Algo:
iterate over the numbers
If negative, skip
If >= len(array), skip
Otherwise, mark array[number-1] as number

'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        def cycle(n):
            nonlocal nums
            if n <= 0 or n > len(nums) or nums[n-1] == n:
                return
            otherNum = nums[n-1]
            nums[n-1] = n
            cycle(otherNum)

        for i in range(len(nums)):
            num = nums[i]
            cycle(num)

        
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1



