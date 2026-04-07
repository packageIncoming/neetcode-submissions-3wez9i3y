class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lhs=[1]* (len(nums)+1)
        rhs = [1]*(len(nums)+1)

        for i in range(len(nums)):
            lhs[i+1]=lhs[i]*nums[i]
        for i in range(len(nums)-1,-1,-1):
            rhs[i] = rhs[i+1] * nums[i]

        res=[]
        for i in range(len(nums)):
            res.append(lhs[i]*rhs[i+1])
        return res
