class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [] # position,speed, time left pairings
        stack = []
        for i in range(len(position)):
            pairs.append([position[i],speed[i], (target-position[i]) / speed[i]])
        pairs.sort(key = lambda x: x[0], reverse=True)
        
        for i in range(len(pairs)):
            if stack and pairs[i][2] <= stack[-1][2]:
                pass
            else:
                stack.append(pairs[i])
        
        return len(stack)