
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b!=0:
            # get carry
            tmp = (a&b) << 1
            # perform addition
            a= (a ^ b) & 0xFFFFFFFF
            b = tmp & 0xFFFFFFFF
        
        return a if a <= 0x7FFFFFFF else ~(a^ 0xFFFFFFFF)
