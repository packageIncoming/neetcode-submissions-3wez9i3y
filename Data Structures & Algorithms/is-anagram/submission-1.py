class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_h = {}
        t_h = {}
        for c in s:
            s_h[c] = s_h.get(c,0) +1
        for c in t:
            t_h[c] = t_h.get(c,0) +1
        for c in set(list(s_h.keys()) + list(t_h.keys())):
            if s_h.get(c,0) == 0 or t_h.get(c,0) == 0:
                return False
            if s_h.get(c,0) != t_h.get(c,0):
                return False
        return True 
        