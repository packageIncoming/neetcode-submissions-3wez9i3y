
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # sorting with custom comparator
        return sorted(sorted(arr,key=lambda elem: (abs(elem-x),elem))[:k])