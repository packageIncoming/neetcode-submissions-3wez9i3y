'''
-stacklike (lifo)
- push adds to the TOP of the stack
- pop REMOVES AND RETURNS MOST FREQUENT ELEMENT

Implementation Idea:
-   Dictionary of key: (freq,insertId)
-   Initialize with insertId of 0, increment whenever something is added 
-
'''

class FreqStack:

    def __init__(self):
        self.elems= {}
        self.insertId = 0

    def push(self, val: int) -> None:
        #O(1)
        self.insertId+=1
        if val in self.elems:
            self.elems[val][0] +=1
            self.elems[val][1].append(self.insertId)
        else:
            self.elems[val] = [1,[self.insertId]]

    def pop(self) -> int:
        #O(n)
        topElem = None
        topElemInsertIndex = float('inf')
        topElemFreq = float('-inf')
        # find most frequent
        for elem in self.elems:
            freq  = self.elems[elem][0]
            insertIdx = self.elems[elem][1][-1]
            if freq > topElemFreq:
                topElemFreq = freq
                topElemInsertIndex = insertIdx
                topElem = elem
            elif freq == topElemFreq and insertIdx > topElemInsertIndex:
                topElemInsertIndex = insertIdx
                topElem = elem
        if topElem:
            self.elems[topElem][0] -=1
            self.elems[topElem][1].pop()
            if self.elems[topElem][0] <=0:
                del self.elems[topElem]
        return topElem
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()