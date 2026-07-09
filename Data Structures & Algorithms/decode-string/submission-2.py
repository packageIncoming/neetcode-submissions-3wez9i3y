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

        num=0
        cur=""

        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num *10 + int(c)
            elif c  == '[':
                numStack.append(num)
                stack.append(cur)
                cur=""
                num=0
            elif c == ']':
                count = numStack.pop()
                tmp = cur
                cur = stack.pop() + tmp*count

            else:
                cur+=c

        return  cur