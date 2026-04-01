class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo = {}
        def permute(i):
            if i > len(s):
                return 0
            if i == len(s):
                return 1
            # now it is in bounds
            # make sure leading char is not 0
            if s[i] == '0':
                return 0 # invalid
            # now check if you can split into 2 paths (1 char or 2 char)
            if i+1 <len(s) and int(s[i:i+2]) <=26:
                return permute(i+1) + permute(i+2)
            else:
                return permute(i+1)
        return permute(0)