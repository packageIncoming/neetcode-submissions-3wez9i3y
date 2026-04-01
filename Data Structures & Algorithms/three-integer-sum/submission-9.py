class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''Algorithm:
            Sort nums
            Iterate over all numbers, -nums[i] is the target
            Initialize l=i+1, r=len(nums)-1
            While l+r > target, move r in
            While l+r < target, move l in
            If l+r == target, add [nums[i],nums[l],nums[r]] to triplets if it is not already in triplets
                Maybe use tuples to avoid having to keep track?

            Break when l ==r
            Return triplets
        '''
        nums.sort()
        triplets = set()
        for i in range(len(nums)):
            target = -nums[i]
            l,r = i+1 ,len(nums)-1
            while l < r:
                while r > l and nums[l] + nums[r] > target:
                    r-=1
                while l < r and nums[l] + nums[r] < target:
                    l+=1
                if l<r and nums[l] + nums[r] == target:
                    triplets.add( (nums[i],nums[l],nums[r]) )
                    l+=1

        return [list(t) for t in triplets]
        