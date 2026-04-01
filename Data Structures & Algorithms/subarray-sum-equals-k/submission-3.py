class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = defaultdict(int)
        prefixes[0]=1
        s = 0
        res=0
        for num in nums:
            s += num# calc prefix sum up to this point
            diff = s-k# figure out what can be chopped off
            if diff in prefixes:
                res+=prefixes[diff]
            prefixes[s] += 1
        return res
            