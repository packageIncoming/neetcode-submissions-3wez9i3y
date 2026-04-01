'''

If a left-moving asteroid is larger than all the current positive ones, does it eliminate all of them 
or just the first one? I'm going to assume it eliminates all of them. 

Therefore negative asteroids basically act as a filter: 
'''


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        vals = []

        for i in range(len(asteroids)):
            a = asteroids[i]
            if a >0:
                vals.append(a)
            else:
                destroyed=False

                while vals and vals[-1] > 0 and vals[-1] <= abs(a):
                    top = vals.pop()
                    if abs(top) == abs(a):
                        destroyed=True
                        break
                if vals and vals[-1] > abs(a):
                    destroyed=True
                if not destroyed:
                    vals.append(a)
        return vals

        