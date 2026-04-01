class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        vals = []

        usedIdxs = [False]*len(nums)
        curPerm = []
        def backtrack():
            if len(curPerm) == len(nums):
                vals.append(curPerm.copy())
                return
            for i in range(len(nums)):
                if usedIdxs[i] is True:
                    continue
                # if the previous value is the same as this one and it has been used, don't use it
                if i-1>-1 and nums[i] == nums[i-1] and usedIdxs[i-1] is True:
                    continue
                # use it
                usedIdxs[i] = True
                curPerm.append(nums[i])
                backtrack()
                # dont use it
                usedIdxs[i]=False
                curPerm.pop()

        backtrack()

        return vals