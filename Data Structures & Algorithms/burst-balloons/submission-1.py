'''
What is the main decision to be made at each index?:
    Decide whether or not to pop the balloon

'''


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def getLeftBalloon(i,seen):
            val = 1
            for j in range(i,-1,-1):
                if j not in seen:
                    return nums[j]
            return val
        def getRightBalloon(i,seen):
            val = 1
            for j in range(i,len(nums)):
                if j not in seen:
                    return nums[j]
            return val

        cache = {}

        def dfs(seen):
            res=0
            if len(seen) == len(nums):
                return 0
            for j in range(len(nums)):
                # at each point we can either decide to pop or not pop if it has not already been popped
                tag = (j,tuple(seen))
                if tag in cache:
                    res = max(res,cache[tag])
                else:
                    if j not in seen:
                        # has not been seen, can be popped
                        seen.add(j)
                        tot = getLeftBalloon(j-1,seen) * nums[j] * getRightBalloon(j+1,seen)
                        cache[tag] = tot+dfs(seen)
                        res = max(res,cache[tag])
                        # then add back to poppables
                        seen.remove(j)
            return res

        return dfs(set())
