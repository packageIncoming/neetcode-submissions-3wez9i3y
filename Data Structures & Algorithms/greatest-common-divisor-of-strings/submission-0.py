class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ""
        SHORTER = str1
        LONGER = str2
        if len(str1) < len(str2):
            SHORTER,LONGER = LONGER,SHORTER

        for i in range(len(SHORTER)):
            sub = SHORTER[:i+1]
            sub_in_shorter = len(SHORTER) // len(sub)
            sub_in_longer = len(LONGER) // len(sub)
            if sub*sub_in_shorter == SHORTER and sub*sub_in_longer == LONGER:
                gcd = sub
        return gcd