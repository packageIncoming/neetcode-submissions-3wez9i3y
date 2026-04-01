class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # solution 2 (from solution video :( )
        nums.sort() #O(nlogn)
        triplets = []
        for i, a in enumerate(nums): #O(n)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l < r: # O(n)
                s = a + nums[l] + nums[r]
                if s > 0:
                    r-=1
                elif s < 0:
                    l+=1
                else:
                    triplets.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1

        return triplets #(O(n^2) time, O(1) space)