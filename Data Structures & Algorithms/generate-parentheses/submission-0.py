class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        done = []
        stack.append(("(",1,0))

        while len(stack) > 0:
            item  = stack.pop()
            if (item[1] + item[2] )== n*2:
                done.append(item[0])
            else:
                if item[1] < n:
                    stack.append( ( item[0]+"(", item[1]+1, item[2]) )
                if item[2] < item[1]:
                    stack.append( ( item[0] + ")", item[1], item[2]+1) )
            
        return done