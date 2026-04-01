class Solution:
    def romanToInt(self, s: str) -> int:
        simpleValues = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        val = 0
        i=0
        while i < len(s):

            char = s[i]
            nxt=s[i+1] if (i+1)<len(s) else ""
            if char+nxt in simpleValues:
                val+=simpleValues[char+nxt]
                i+=1
            else:
                val+=simpleValues[char]
            #print(char+nxt,val)
            i+=1

        return val