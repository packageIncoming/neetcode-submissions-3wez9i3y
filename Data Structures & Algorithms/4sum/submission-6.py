'''
sort the numbers
[-3,0,1,2,3,3]

'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        cur=[]
        def kSum(k,startIdx,target):
            if k!=2:
                for i in range(startIdx,len(nums)-k+1):
                    if nums[i] == nums[i-1] and i>startIdx: continue
                    cur.append(nums[i])
                    kSum(k-1,i+1,target-nums[i])
                    cur.pop()
                return
            l,r = startIdx,len(nums)-1
            while l<r:
                while l<r and nums[l]+nums[r] <target:
                    l+=1
                while l<r and nums[l]+nums[r] > target:
                    r-=1
                if l<r and  nums[l]+nums[r] == target:
                    res.append(cur+[nums[l],nums[r]])
                l+=1
                while l<r and nums[l] == nums[l-1]:
                    l+=1
        kSum(4,0,target)
        return res                
