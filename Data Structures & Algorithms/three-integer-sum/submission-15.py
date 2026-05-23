'''
nums[i]+nums[j]+nums[k]==0
k is the largest
-nums[k] == nums[i]+nums[j]

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        trips = []
        print(nums)
        k=len(nums)-1
        while k>1:
            l,r = 0,k-1
            while l<r:
                if nums[l]+nums[r] == -nums[k]:
                    trips.append([nums[l],nums[r],nums[k]])
                    t = nums[l]
                    while nums[l]==t and l < r:
                        l+=1
                if nums[l]+nums[r]> -nums[k]:
                    r-=1
                elif nums[l]+nums[r] < -nums[k]:
                    l+=1
            t=nums[k]
            k-=1
            while nums[k] == t and k > 1:
                k-=1
        return trips