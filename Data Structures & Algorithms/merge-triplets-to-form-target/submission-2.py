class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        currState = [False,False,False]
        finds=0
        for i in range(len(triplets)):
            trip = triplets[i]
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]: continue
            for i in range(3):
                if trip[i] == target[i] and currState[i] == False:
                    finds+=1
                    currState[i] = True
            if finds == 3: return True
        return False