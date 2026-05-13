class Solution:
    def reverseBits(self, n: int) -> int:
        s = [c for c in f"{n:032b}"]
        print(s)

        for i in range(16):
            s[i],s[31-i] = s[31-i],s[i]

        return int(''.join(s),2)