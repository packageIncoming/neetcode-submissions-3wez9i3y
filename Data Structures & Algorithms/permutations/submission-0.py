class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permuteStartingFromIndex(idx):
            # base case: idx==len(nums)-1 => returns a single array [nums[idx]]
            if idx == len(nums)-1:
                return [[nums[idx]]]
            # get permutations of remainder:
            otherPermutations = permuteStartingFromIndex(idx+1)
            createdPermutations = [] # the permutations to be created on this call
            # for each permutation returned, 
            for p in otherPermutations:
                # insert the current index into every possible position 
                for i in range(len(p)+1):
                    newP = p.copy()
                    newP.insert(i,nums[idx])
                    createdPermutations.append(newP)
            return createdPermutations 
        
        return permuteStartingFromIndex(0)