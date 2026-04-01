class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums)/3
        res=[]
        m = defaultdict(int)
        for num in nums:
            if m[num] == -1: continue
            m[num]+=1
            if m[num] > target:
                res.append(num)
                m[num]=-1
        return res