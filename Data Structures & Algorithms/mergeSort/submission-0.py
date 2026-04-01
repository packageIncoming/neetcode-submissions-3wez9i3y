# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        #Base case: arr of len 1 is technically sorted
        if len(pairs) <= 1:
            return pairs
        middle_i = len(pairs)//2
        #Recursive calls to sort lefthand and righthand 
        left = self.mergeSort(pairs[0:middle_i])
        right = self.mergeSort(pairs[middle_i:len(pairs)])

        #Merging process: iterate over left and right 
        arr = []
        l_ptr = 0
        r_ptr = 0
        while l_ptr < len(left) and r_ptr < len(right):
            l_pair = left[l_ptr]
            r_pair = right[r_ptr]
            if l_pair.key <= r_pair.key:
                arr.append(l_pair)
                l_ptr+=1
            else:
                arr.append(r_pair)
                r_ptr+=1
        #In the case where len(left) != len(right), iterate over
        # what would be the remaining items and append them
        while l_ptr < len(left):
            arr.append(left[l_ptr])
            l_ptr+=1
        while r_ptr < len(right):
            arr.append(right[r_ptr])
            r_ptr+=1
        return arr

        
