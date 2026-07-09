'''
intial idea:
two stacks
one that has the numbers
one that has the strings

when you get to a number, consume it 
when you reach a [ convert the current number being made into an int
and put it on the stack




'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        numStack = []

        numStr = ""

        for i in range(len(s)):
            c = s[i]
            if c in "1234567890":
                numStr += c
            elif c  == '[':
                numStack.append(int(numStr))
                stack.append('[')
                numStr = ''
            elif c == ']':
                num = numStack.pop()
                r = ''
                while stack:
                    v = stack.pop()
                    if v == '[':break
                    r= v + r
                r*=num
                stack.append(r)
            else:
                stack.append(c)

        return  "".join(stack)