class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res=0
        for o in operations:
            if o == '+':
                stack.append(stack[-1]+stack[-2])
                res+=stack[-1]
            elif o == 'D':
                stack.append(stack[-1]*2)
                res+=stack[-1]
            elif o == 'C':
                res-=stack[-1]
                stack.pop()
            else:
                stack.append(int(o))
                res+=stack[-1]
        return res