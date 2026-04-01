'''
Goal: Return the maximum number of stones Alice can get
-   There's a number of piles arranged in a row
-   Each pile has a positive # stones piles[i]
-   Each player can take up to the first X piles,
        1<=X<=2M
        M= max(M,X)
        M= 1 to start
- Alice starts first
- Both play optimally

Input example
piles = [3,1,2,5,7]
Alice takes 3, X=1, M= max(1,1)=1
Bob takes 1; X=1, M= max(1,1)=1
Alice takes 2 and 5; X=2, M=max(1,2)=2
Bob takes 7; X=1, M=max(2,1)=2
END
Alice=10, Bob=8

Would greedy work?
Assuming greedy means to take as many as you can on your turn, 
then NO. 
From above
Alice takes 3 and 1, then Bob takes 2 and 5 and 7

How about a recursion tree?
- Keep track of who's turn it is
- Keep track of M
- Keep track of current index
- Keep track of score (as the return value) of Alice and maybe Bob too?

From 1 to 2M,
    Get the potential score by consuming j stones starting at i
    Add to corresponding player's score
    Recurse starting at i+j+1 stones for the other player
End condition is when i = len(stones) so return aliceScore


'''

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        memo = {}

        def recurse(alice,i,m):
            if i >= len(piles):
                return 0
            if (alice,i,m) in memo:
                return memo[(alice,i,m)]

            highScore=0 if alice else float('inf')

            subTot = 0 
            for x in range(1,2*m+1):
                # calculate the potential score
                if i+x > len(piles):
                    break
                subTot += piles[i+x-1]
                newM = max(m,x)
                if alice:
                    # add to the total
                    highScore = max(highScore,subTot+recurse(not alice, i+x,newM))
                else:
                    # just continue from here
                    highScore = min(highScore,recurse(not alice, i+x, newM))
            memo[(alice,i,m)] = highScore
            return highScore

        return recurse(True, 0,1)

                

        
        