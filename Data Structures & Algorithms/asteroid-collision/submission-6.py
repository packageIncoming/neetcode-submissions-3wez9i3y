'''
If a negative asteroid shows up & the current list is empty then just add that asteroid
otherwise remove
'''


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res= []
        for a in asteroids:
            if a <0:
                #-
                alive=True
                while res and res[-1]>0:
                    if res[-1]==abs(a):
                        res.pop()
                        alive=False
                        break
                    elif res[-1]>abs(a):
                        alive=False
                        break
                    else:
                        res.pop()
                if alive:
                    res.append(a)
            else:
                res.append(a)

        return res