'''
2[abc]
nums = []
strs = []

curNum , curStr

we reach [
-> add 2 to nums nums = [2]
-> add curStr to strs

start creating 

we reach ]
-> pop the previous string we had into temp
cur = temp + cur*curNum
curNum = nums.pop()

'''

class Solution:
    def decodeString(self, s: str) -> str:
        strs = []
        nums = []

        curNum = 0
        curStr = ""
        for c in s:
            if c.isdigit():
                curNum = curNum*10+int(c)
            elif c == '[':
                strs.append(curStr)
                curStr=""
                nums.append(curNum)
                curNum=0
            elif c == ']':
                temp = curStr
                curStr = strs.pop() +temp*nums.pop() 
            else:
                curStr += c

        return curStr