class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        def findCombinations(curSum,combination,idx):
            if curSum > target:
                return
            if curSum == target:
                combinations.append(combination.copy())
                return
            for i in range(idx,len(nums)):
                combination.append(nums[i])
                curSum += nums[i]
                findCombinations(curSum,combination,i)
                combination.pop()
                curSum-= nums[i]

        findCombinations(0,[],0)
                
        return combinations