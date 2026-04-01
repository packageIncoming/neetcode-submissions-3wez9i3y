class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=""

        aPtr = len(a)-1
        bPtr = len(b)-1

        # add both
        cin = 0
        while aPtr >-1 and bPtr > -1:
            aDigit = int(a[aPtr])
            bDigit = int(b[bPtr])
            print(f"{aDigit} + {bDigit} + {cin}")
            s = aDigit+bDigit+cin
            if s == 3:
                res = res + "1"
                cin=1
            elif s == 2:
                res = res + "0"
                cin=1
            elif s == 1:
                res = res + "1"
                cin=0
            elif s == 0:
                res = res + "0"
                cin=0
            aPtr-=1
            bPtr-=1
        print(res)
        # add remainder of a
        while aPtr >-1 :
            aDigit = int(a[aPtr])
            s = aDigit+cin
            if s == 3:
                res = res + "1"
                cin=1
            elif s == 2:
                res = res + "0"
                cin=1
            elif s == 1:
                res = res + "1"
                cin=0
            elif s == 0:
                res = res + "0"
                cin=0
            aPtr-=1

        # add remainder of b
        while bPtr >-1 :
            bDigit = int(b[bPtr])
            s = bDigit+cin
            if s == 3:
                res = res + "1"
                cin=1
            elif s == 2:
                res = res + "0"
                cin=1
            elif s == 1:
                res = res + "1"
                cin=0
            elif s == 0:
                res = res + "0"
                cin=0
            bPtr-=1
        if cin == 1:
            res += "1"
        return res[::-1]