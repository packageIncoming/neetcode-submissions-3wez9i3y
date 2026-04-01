class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            newN = 0
            while n >= 1:
                val = (n%10)**2
                newN+=val
                n = n // 10
            if newN in seen:
                return False
            seen.add(newN)
            n=newN

        return True