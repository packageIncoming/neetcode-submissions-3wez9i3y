class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # what is the locally optimal decision to make at each point?
        # If merging gets you closer to target then merge, otherwise don't merge
        currState = [0,0,0]

        for i in range(len(triplets)):
            trip = triplets[i]
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]: continue
            merged = [
                max(trip[0],currState[0]),
                max(trip[1],currState[1]),
                max(trip[2],currState[2])
            ]
            currCloseness = sum([currState[i] == target[i] for i in range(len(target))])
            mergeCloseness = sum([merged[i] == target[i] for i in range(len(target))])
            if mergeCloseness >= currCloseness:
                currState = merged
        if sum([currState[i] == target[i] for i in range(len(target))]) == len(target):
            return True
        return False