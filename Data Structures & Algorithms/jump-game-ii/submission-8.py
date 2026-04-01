class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1: return 0
        curJumps=0
        l,r=0,0
        while r < len(nums)-1:
            print(f"Range: {l} to {r}")
            highest = 0
            for i in range(l,r+1):
                highest = max(highest,i+nums[i])
            l=r+1
            r=highest
            curJumps+=1
        return curJumps