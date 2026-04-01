class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1: return [0] # edge case
        res = [0]*len(temperatures)
        stack = [] # index, temperature pairs
        for i,temp in enumerate(temperatures):
            while stack and stack[-1][-1] < temp:
                item  = stack.pop()
                res[item[0]] = i - item[0]
            stack.append((i,temp))


        return res