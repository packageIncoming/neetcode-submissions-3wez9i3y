'''
Goal: Find # of combinations of the integers in nums[] that sum up to target

Target can be up to 1000

My IMMEDIATE reaction/instinct is dynamic programming



'''


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = [0]*(target+1)
        memo[0] = 1 # acts as an awkward but effective base case
        #memo[target] is the result
        for i in range(1,target+1):
            for num in nums:
                if i-num >=0:
                    memo[i] += memo[i-num]
        return memo[target]