
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # two pointers
        l,r = 0,len(arr)-1

        while r-l+1>k:
            lDist = abs(arr[l]-x)
            rDist = abs(arr[r]-x)
            if rDist < lDist:
                l+=1
            else:
                r-=1 

        return arr[l:r+1]