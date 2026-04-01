class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_hash = defaultdict(int)
        t_hash = defaultdict(int)
        for i in range(len(s)):
            s_hash[s[i]] +=1
            t_hash[t[i]]+=1 
        for key in set(s_hash.keys()).union(set(t_hash.keys())):
            if s_hash[key] == 0 or t_hash[key] == 0 or s_hash[key] != t_hash[key]:
                return False
        return True