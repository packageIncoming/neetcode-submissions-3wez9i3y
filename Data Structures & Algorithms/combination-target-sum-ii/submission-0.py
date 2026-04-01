class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []
        def backtrackingDFS(i,curCombination,curSum):
            if curSum == target:
                combinations.append(curCombination.copy())
                return # success case
            if curSum > target or i >= len(candidates):
                return # fail case
            # recursive case
            # decide WITH
            curCombination.append(candidates[i])
            curSum+= candidates[i]
            curC = candidates[i]

            backtrackingDFS(i+1,curCombination,curSum)
            # decide withOUT
            curCombination.pop()
            curSum-= curC
            i+=1
            while i < len(candidates) and candidates[i] == curC:
                i+=1
            backtrackingDFS(i,curCombination,curSum)
        backtrackingDFS(0,[],0)
        return combinations