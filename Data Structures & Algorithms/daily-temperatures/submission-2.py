class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)

        stack=[]
        #(temp,i)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and temp> stack[-1][0]:
                r = stack.pop()
                res[r[1]] = i - r[1]
            stack.append((temp,i))

        return res