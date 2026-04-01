'''
A square has 4 equal-length sides

Sum(matchsticks) must be divisble by 4 as a simple check
Len(matchsticks) must be at least 4 to make the 4 sides
Each matchstick can be used only once and they MUST be used
Recursion is the first thing that comes to mind, 0/1 bound knapsack 


'''

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if (total %4 != 0) or len(matchsticks) < 4:
            return False
        
        sideTarget = total //4
        usedMask = [0]*len(matchsticks)
        usedCount=0

        def make(i,target,k):
            nonlocal usedMask
            nonlocal usedCount
            if k ==0 and usedCount == len(matchsticks):
                return True 

            if target ==0:
                return make(0,sideTarget,k-1)

            
            for j in range(i,len(matchsticks)):
                if target - matchsticks[j] >= 0 and usedMask[j] != 1:
                    # use it
                    usedMask[j] = 1
                    
                    usedCount +=1
                    if make(j+1,target-matchsticks[j],k):
                        return True
                    # don't use it
                    usedMask[j] = 0
                    usedCount-=1
            return False # did not succeed

        return make(0,sideTarget,4)




