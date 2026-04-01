class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        s_arr = [0]*26
        t_arr = [0]*26
        for i in range(len(s)):
            pos_s=ord(s[i])-ord('a')        
            pos_t = ord(t[i])-ord('a')
            s_arr[pos_s]+=1
            t_arr[pos_t]+=1
        for i in range(26):
            if s_arr[i] != t_arr[i]:
                return False
        return True