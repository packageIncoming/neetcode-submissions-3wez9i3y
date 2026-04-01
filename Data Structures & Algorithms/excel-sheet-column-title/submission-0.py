class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out=""
        # ASCII 'A' = 65

        while columnNumber > 0:
            columnNumber-=1
            d = columnNumber % 26
            out = chr(d+65)+out
            columnNumber //=26

        return out