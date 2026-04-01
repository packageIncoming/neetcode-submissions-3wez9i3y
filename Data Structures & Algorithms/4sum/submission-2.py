class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # there's no way this isn't backtracking
        # indices can be distinct but values cannot
        nums.sort()
        arrs=[]

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue # Dont re-use 
            for j in range(i+1,len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue # Dont re-use 
                l,r = j+1, len(nums)-1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        arrs.append([nums[i] , nums[j] , nums[l] , nums[r]])
                        l+=1
                        r-=1
                        while l < len(nums) and nums[l] == nums[l-1]:
                            l+=1
                        while r > -1 and nums[r] == nums[r+1]:
                            r-=1
                    elif total < target:
                        l+=1
                    elif total > target:
                        r-=1

        return arrs