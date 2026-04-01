from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        n = len(senate)
        rQ,dQ = deque(),deque()
        # add to deques
        for i in range(len(senate)):
            if senate[i] == "D":
                dQ.append(i)
            else:
                rQ.append(i)

        while rQ and dQ:
            r = rQ.popleft()
            d = dQ.popleft()
            if r < d:
                # remove d 
                rQ.append(r+n)
            else:
                # remove r
                dQ.append(d+n)
        if len(rQ) ==0:
            return "Dire"
        else:
            return "Radiant"
