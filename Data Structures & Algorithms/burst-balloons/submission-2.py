'''
What is the main decision to be made at each index?:
    Decide whether or not to pop the balloon

'''


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        cache = {}

        def dfs(l,r):
            if l > r:
                return 0
            if (l,r) in cache:
                return cache[(l,r)]
            cache[(l,r)] = 0
            for j in range(l,r+1):
                    tot = nums[l-1] * nums[j] * nums[r+1]
                    tot += dfs(l,j-1)+dfs(j+1,r)
                    cache[(l,r)] = max(cache[(l,r)],tot)
            return cache[(l,r)]

        return dfs(1,len(nums)-2)
