class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            l = len(s)
            output += f"{l}#"
            output +=s 
        return output
    def decode(self, s: str) -> List[str]:
        strs = []
        ptr = 0
        # Encoded string should come in the format (length)#(characters)
        # 1. get length
        # 2. split on delimiter
        # 3. Iterate length
        while ptr < len(s):
            len_str = ""
            while s[ptr] != "#":
                len_str += s[ptr]
                ptr+=1
            l = int(len_str)
            ptr+=1
            cur_str = ""
            for i in range(l):
                cur_str += s[ptr]
                ptr+=1
            strs.append(cur_str)


        return strs