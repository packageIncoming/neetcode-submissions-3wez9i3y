class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        def run(lBound,rBound):
            dp0 = 0
            dp1=  0
            for i in range(rBound,lBound-1,-1):
                skipCur = dp0
                takeCur = nums[i] + dp1
                dp1 = dp0
                dp0 = max(skipCur,takeCur)
            return dp0
        fromFirst  =run(0,len(nums)-2)
        fromSecond = run(1,len(nums)-1)
        return max(fromFirst,fromSecond)
