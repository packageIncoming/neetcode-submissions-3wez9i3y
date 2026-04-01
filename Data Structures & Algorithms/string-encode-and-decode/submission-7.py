class Solution:
    CAESAR_OFFSET = 5
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            encoded = "".join(chr(ord(c) + self.CAESAR_OFFSET) for c in s)
            res.append(f"{len(encoded)}#{encoded}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            decoded = "".join(chr(ord(c) - self.CAESAR_OFFSET) for c in word)
            res.append(decoded)
            i = j+1+length
        return res

