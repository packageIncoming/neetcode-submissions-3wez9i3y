class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen  ={}
        for i in range(len(nums)):
            other = target-nums[i]
            if other in seen:
                return [seen[other],i]
            else:
                seen[nums[i]]=i