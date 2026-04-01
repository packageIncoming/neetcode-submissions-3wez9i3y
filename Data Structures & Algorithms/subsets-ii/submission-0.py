class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []

        def getSubsets(idx,curCombination):
            # base case: idx == len(nums) meaning we have checked all items so append and return
            if idx == len(nums):
                subsets.append(curCombination.copy())
                return
            # solutions WITH element at index
            curCombination.append(nums[idx])
            getSubsets(idx+1,curCombination)
            # solutions WITHOUT element at index
            curCombination.pop()
            j = idx
            while j < len(nums) and nums[j] == nums[idx]:
                j+=1
            getSubsets(j,curCombination)
        getSubsets(0,[])
        return subsets