class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #solution 1: brute-force solution
        triplets = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k  in range(j+1,len(nums)):
                    cur_sum = nums[i] + nums[j] + nums[k]
                    if cur_sum == 0:
                        l = tuple(sorted((nums[i],nums[j],nums[k])))
                        if l not in triplets:
                            triplets.add(l)
        return [list(l) for l in triplets]