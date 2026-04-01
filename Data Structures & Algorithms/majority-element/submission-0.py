class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        goal = len(nums)/2
        hmap = defaultdict(int)
        for num in nums:
            hmap[num]+=1
            if hmap[num]>goal:
                return num