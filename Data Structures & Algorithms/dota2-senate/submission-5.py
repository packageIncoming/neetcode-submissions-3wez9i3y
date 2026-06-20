'''
This seems like a stack type of problem

Round based procedure, assume everyone acts optimally

Ordering does matter from the look of it

It's not just a matter of who has more 

Idea:
Stack+ keeping track of how many bans are for each?
If you get R and RBans>0 then skip that one
Otherwise increment DBans and add that R back into play

But senate's length can be pretty big (10k)

Also how do you know when to quit?

you could turn the senate into a list & have some market for "skip this guy"

Let's walk through an example

R-R-D-D-D

Not a stack a queue!
'''
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque()

        rCount=0
        dCount=0
        # populate queue
        for c in senate:
            if c== 'R':
                rCount+=1
            if c== 'D':
                dCount+=1
            q.append(c)
        
        rBans=0
        dBans=0

        while q:
            if rCount==0 or dCount==0: break
            top = q.popleft()
            if top == 'R':
                if rBans>0:
                    rCount-=1
                    rBans-=1
                else:
                    q.append(top)
                    dBans+=1
            elif top == 'D':
                if dBans>0:
                    dCount-=1
                    dBans-=1
                else:
                    q.append(top)
                    rBans+=1
        
        if rCount==0:
            return 'Dire'
        else:
            return "Radiant"


        


        