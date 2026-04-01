'''
mountain array
    - 'peak' at index i, where elements arr[0:i] < arr[i], 
    and elements arr[i+1:] > arr[i]
    - we  are guaranteed values are either strictly increasing or decreasing

    - easy way to check if an index k is the peak:
        if arr[k-1] < arr[k], and arr[k+1] > arr[k] and k < len(arr)-1
            then we have found the peak
    -we can also set up bounds for lefthand side and righthand side of the mountain
        if arr[k] is the peak then 0:k is the left, k+1:len(arr) is the right
    - we can set these after finding the peak
    -we can tell what half (left or right) we are in by checking the current value 
        - if arr[k-1] < arr[k] < arr[k+1] we are ascending and therefore in the left
        - if arr[k-1] > arr[k] > arr[k+1] we are descending and therefore in the right







'''

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        def findPeak(mountain)->int:
            l, r = 1, mountain.length()-2
            peak=0
            while l <=r:
                mid = (l+r)//2
                left,m,right = mountain.get(mid-1),mountain.get(mid),mountain.get(mid+1)

                if left < m < right:
                    # in left side so move up
                    l=mid+1
                elif left > m > right:
                    # in right side so move down
                    r=mid-1
                else:
                    peak=mid
                    break
            return peak
        
        def findValueLeft(l,r,mountain,value)->int: # l inclusive, r inclusive
            while l <=r:
                mid = (l+r)//2
                midVal = mountain.get(mid)
                if midVal == value:
                    return mid
                elif midVal > value:
                    r=mid-1
                else:
                    l=mid+1
            return -1
        
        def findValueRight(l,r,mountain,value)->int: # l inclusive, r inclusive
            while l <=r:
                mid = (l+r)//2
                midVal = mountain.get(mid)
                print(midVal)
                if midVal == value:
                    return mid
                elif midVal > value:
                    l=mid+1
                else:
                    r=mid-1
            return -1

        peakIdx = findPeak(mountainArr)
        peakVal = mountainArr.get(peakIdx)

        if target == mountainArr.get(peakIdx):
            return peakIdx

        leftAttempt = findValueLeft(0,peakIdx-1,mountainArr,target)

        if leftAttempt != -1:
            return leftAttempt
        else:
            return  findValueRight(peakIdx+1,mountainArr.length()-1,mountainArr,target)

        