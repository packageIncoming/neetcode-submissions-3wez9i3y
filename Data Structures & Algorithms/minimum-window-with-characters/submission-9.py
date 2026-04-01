class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        # turn t into hashmap
        t_map = defaultdict(int)
        for i in range(len(t)):
            t_map[t[i]] +=1
        l = 0
        # begin iterating over s to find min substring
        s_map = defaultdict(int)
        needs = len(t_map)
        haves = set()
        min_len = float('inf')
        min_substring = ""
        for r in range(len(s)):
            s_map[s[r]]+=1
            if s[r] not in haves and s[r] in t_map and s_map[s[r]] == t_map[s[r]]:
                #print(f"fulfilled requirement: {s[r]}")
                haves.add(s[r])
            while len(haves) == needs:
                # shrink from the left
                if (r-l)+1 < min_len:
                    min_len = (r-l)+1
                    min_substring = s[l:r+1]
                s_map[s[l]] -=1
                if s[l] in haves and s_map[s[l]] < t_map[s[l]]:
                    haves.remove(s[l])
                l+=1
        return min_substring