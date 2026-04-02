'''

What sticks out to me?:
    -Dynamic programming obviously, could either be bottom-up or top-down
    -Don't have to return the actual decodings, just the # of ways it can be decoded
    -If the next digit is a 0 then the decoding MUST be current+next since 01..09 is not 
    valid


How would I solve this as a human?:
ex. 1012:

i=0 decode(0)
get current val: 1
get next val if in bounds: 0
is the next value a 0? YES
then I MUST decode as a pair, only 1 way, so return decode(i+2)

i=2 decode(i+2)
get current val: 1
get next val if in bounds: 2
is the next value a 0? NO
then I can either decode this as a 1 or a 12
so we return decode(i+1) + decode(i+2)

i=3 (decode i+1)
get current val: 2
get next: NULL
is the next value a 0? NO
is there a next? NO
so I can only decode this one way
so return decode(i+1)

i=4 (decode(i+2)) from i=2
OOB, return 1 (represents successful decode)

i=4 (decode(i+1)) from i=3
OOB, return 1

So there are 2 ways to decode

What is the changing variable? i
So when we memoize we can use i 


'''


class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def decode(i):
            if i >= len(s):
                return 1
            if i in memo:
                return memo[i]
            if s[i] == '0': return 0
            cur = s[i]
            nxt= s[i+1] if (i+1)< len(s) else None
            res= decode(i+1)
            if i+1<len(s):
                if 10<= int(s[i:i+2]) <=26:
                    res+= decode(i+2)

            memo[i]= res
            return memo[i]


        return max(0,decode(0))
        