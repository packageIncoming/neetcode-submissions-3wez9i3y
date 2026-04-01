class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 != 0: return False
        pairs = {
            '[':']',
            '{':'}',
            '(':')'
        }
        opens = []
        for c in s:
            if c in pairs.keys():
                opens.append(c)
            elif c in pairs.values():
                if len(opens) == 0 or  pairs[opens.pop()] != c:
                    return False
        if len(opens) > 0: return False
        return True