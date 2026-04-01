class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ptrArr = [0]*len(strs)
        longest = ""

        while True:
            char = None
            for i in range(len(ptrArr)):
                s = strs[i]
                ptr = ptrArr[i]
                if ptr >= len(s):
                    return longest 
                if char is None:
                    char = s[ptr]
                else:
                    if char != s[ptr]:
                        return longest
                ptrArr[i]+=1
            longest+=char

        return longest