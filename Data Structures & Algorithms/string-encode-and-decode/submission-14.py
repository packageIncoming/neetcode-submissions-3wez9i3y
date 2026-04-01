class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        delim = "/x"
        delim_num = "/"
        for s in strs:
            res += delim + str(len(s)) + delim_num + s
        return res
    # gives something like /x5/Hello/x5/World

    def decode(self, s: str) -> List[str]:
        res= []

        delim = "/x"
        delim_num = "/"

        i=0
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] == delim:
                # now extract num
                num_str = ""
                i+=2
                while i < len(s) and s[i]!=delim_num:
                    num_str+=s[i]
                    i+=1
                l = int(num_str)
                # now i points at delim_num ('/')
                # the string goes from s[i+1:i+1+l]
                res.append(s[i+1:i+1+l])
                # next delim starts at i+1+l
                i = i+1+l


        return res