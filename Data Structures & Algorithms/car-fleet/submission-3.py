
'''


t=10, pos = [1,4] spd = [3,2]
order by pos:
[(1,4),(3,2)]
will take (3,2) 4 turns to get to 10 (5 7 9 11)
will take (1,4) 3 turns to get to 10 (5 9 13)
pop while turns <= current amount of turns

t=10, pos = [4,1,0,7] spd = [2,2,1,1]
sort and item[2] = # turns to get to t
[(0,1,10),(1,2,4),(4,2,3),(7,1,3)]
3 fleets


'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p = [[position[i],speed[i],(target - position[i]) / speed[i]] for i in range(len(position))]
        p.sort()
        res=0
        while p:
            top = p.pop()
            res+=1
            while p and p[-1][2] <= top[2]:
                p.pop()
        return res
