from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newDigits = deque()
        cin = 1
        for i in range(len(digits)-1,-1,-1):
            newV= digits[i] +cin
            if newV == 10:
                newDigits.appendleft(0)
                cin=1
            else:
                cin=0
                newDigits.appendleft(newV)
        
        if digits[0] + cin == 10:
            newDigits.appendleft(1)

        return list(newDigits)