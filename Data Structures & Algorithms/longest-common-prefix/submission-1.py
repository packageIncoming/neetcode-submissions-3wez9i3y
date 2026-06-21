class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ptrs=[0 for i in range(len(strs))]
        res=""
        while True:
            prev=None
            for i in range(len(ptrs)):
                s = strs[i]
                if ptrs[i] >= len(s):
                    return res
                if prev and prev != s[ptrs[i]]:
                    return res
                if not prev:
                    prev = s[ptrs[i]]
                ptrs[i]+=1
            res+=prev