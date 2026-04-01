class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #from constraints, num1 and num2 are non-negative and they do not contain leading 0s
        def multHelper(a,b):
            a_val = ord(a)-48
            b_val = ord(b)-48
            return a_val*b_val

        LONGER,SHORTER = num1,num2
        if len(num2) > len(num1):
            LONGER,SHORTER = SHORTER,LONGER # just flip
        res=0

        for i in range(len(SHORTER)-1,-1,-1):
            cur_sum = 0
            for j in range(len(LONGER)-1,-1,-1):
                cur_sum += multHelper(SHORTER[i],LONGER[j]) * 10**(len(SHORTER)-(i+1)) * 10**(len(LONGER)-(j+1))
            res+=cur_sum

        return str(res)