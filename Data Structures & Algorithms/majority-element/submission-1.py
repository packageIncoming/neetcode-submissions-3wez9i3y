class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f=defaultdict(int)
        for n in nums:
            f[n]+=1
            if f[n]>= len(nums)/2:
                return n