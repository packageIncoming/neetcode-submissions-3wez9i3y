class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def createCombinationsBacktrack(curComb,i):
            if len(curComb) == k:
                combinations.append(curComb.copy())
                return
            if i > n:
                return
            # decision WITH i
            curComb.append(i)
            createCombinationsBacktrack(curComb,i+1)
            # decision WITHOUT i
            curComb.pop()
            createCombinationsBacktrack(curComb,i+1)
        createCombinationsBacktrack([],1)

        return combinations