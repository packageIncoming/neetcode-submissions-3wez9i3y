class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # there's no way this isn't backtracking
        # indices can be distinct but values cannot
        nums.sort()
        print(nums)
        arrs=[]
        def backtrack(idx,curCollection,curSum):
            if idx >= len(nums) or len(curCollection)==4:
                if curSum == target and len(curCollection)==4:
                    nonlocal arrs
                    arrs.append(curCollection.copy())
                return
            # choose to include
            curCollection.append(nums[idx])
            backtrack(idx+1,curCollection,curSum+nums[idx])

            # choose not to include
            orig = nums[idx]
            while idx < len(nums) and nums[idx] == orig:
                idx+=1
            curCollection.pop()
            backtrack(idx,curCollection,curSum)
        
        backtrack(0,[],0)
        return arrs