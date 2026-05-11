class Solution:
    def isValid(self, s: str) -> bool:
        opens = []
        h = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for i in range(len(s)):
            if s[i] in '({[':
                opens.append(s[i])
            else:
                if len(opens)<1:
                    return False
                top = opens.pop()
                if top != h[s[i]]:
                    return False
        return len(opens)==0
