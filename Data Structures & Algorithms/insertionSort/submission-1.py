# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        #Insertion sort:
        #Check left values and find where to begin swapping
        # At i, if i-1 is sorted properly compared to i then 0 to i-1 is 
        #   already sorted and there is no need to check (terminate while loop for arr[i])
        if len(pairs) == 0:
            return []
        states = []
        states.append(pairs.copy())
        for i in range(1,len(pairs)):
            j= i-1
            while j >= 0 and pairs[j+1].key < pairs[j].key:
                temp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = temp
                j-=1
            states.append(pairs.copy())
        
        return states