class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if visited.get(complement,-1) != -1:
                return sorted([i,visited[complement]])
            visited[num] = i