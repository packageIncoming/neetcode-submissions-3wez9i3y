class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo = {len(s):1}
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
            if i not in self.memo:
                if i+1 <len(s) and int(s[i:i+2]) <=26:
                    self.memo[i] =  permute(i+1) + permute(i+2)
                else:
                    self.memo[i] = permute(i+1)
            return self.memo[i]
        return permute(0)