# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def qsHelper(self,pairs: List[Pair],s:int,e:int):
        # Base case of length 1 (already sorted)
        if ((e-s)+1)<=1:
            return 
        pivot = pairs[e] # Naive approach of choosing rightmost value as pivot
        left = s # Left points to where the values will be stored that are <= pivot
        #Iterate over the array, moving vals <= pivot to the left
        for i in range(s,e):
            if pairs[i].key < pivot.key:
                temp = pairs[left]
                pairs[left]  =pairs[i]
                pairs[i] = temp
                left+=1
        #Perform final swap
        pairs[e] = pairs[left]
        pairs[left] = pivot
        self.qsHelper(pairs,s,left-1)
        self.qsHelper(pairs,left+1,e)
        

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.qsHelper(pairs,0,len(pairs)-1)
        return pairs