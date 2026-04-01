class Solution:
    def countBits(self, n: int) -> List[int]:
        def singleCount(num):
            count=0
            while num >0:
                if num%2==1:
                    count+=1
                num=num>>1
            return count
        return [singleCount(number) for number in range(n+1)]