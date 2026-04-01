class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 != 0: return False
        pairing = {'(':')','[':']','{':'}'}
        stack = []
        for i in range(len(s)):
            p = s[i]
            if p in '({[':
                stack.append(p)
            elif p in ')}]':
                if len(stack) == 0: return False
                item = stack.pop()
                if pairing[item] != p: return False
        if len(stack) > 0: return False
        return True