from collections import deque
class Solution:
    def checkValidString(self, s: str) -> bool:
        lefts=deque()
        stars = deque()
        for i,char in enumerate(s):
            if char == "*":
                stars.append(i)
            elif char =="(":
                lefts.append(i)
            elif char == ")":
                if len(lefts)>0:
                    lefts.pop()
                elif len(stars)>0:
                    stars.pop()
                else:
                    return False
        print(lefts,stars)
        while lefts:
            l = lefts.pop()
            if len(stars) ==0: return False
            star = stars.pop()
            if star < l:
                return False
        return True