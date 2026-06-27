class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        e=1

        i=0

        while i < len(nums) and nums[i] <=0:
            i+=1


        while i < len(nums):
            if i>0 and  nums[i] == nums[i-1]:
                i+=1
                continue
            if nums[i] == e:
                e+=1
                i+=1
            else:
                break


        return e