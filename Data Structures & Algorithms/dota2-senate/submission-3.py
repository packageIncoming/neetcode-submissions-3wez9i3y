from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        d = deque()
        # add all senators first
        for s in senate:
            d.append(s)
        # now begin rounds
        rPass=0
        dPass=0
        while d:
            rCount=0
            dCount=0
            for i in range(len(d)):
                senator = d.popleft()
                if senator == "R":
                    if rPass > 0:
                        # skip senator
                        rPass-=1
                        continue
                    else:
                        # don't skip this but skip the next D
                        rCount+=1
                        dPass+=1
                        d.append(senator) # didnt get skipped
                elif senator == "D":
                    if dPass > 0:
                        # skip
                        dPass-=1
                        continue
                    else:
                        # dont skip this but skip the next R
                        dCount+=1
                        rPass+=1
                        d.append(senator) # didnt get skipped
            #print(rCount,dCount)
            #print(len(d))
            if rCount > dCount and rCount ==len(d):
                return "Radiant"
            elif dCount > rCount and dCount == len(d):
                return "Dire"
