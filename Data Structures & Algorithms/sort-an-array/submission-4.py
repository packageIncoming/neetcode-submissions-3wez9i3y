'''
merge sort attempt

how does merge sort go??

sort left

sort right
zipper merge both 
return zipper merged result

base case?
[]-> []
[1]->[1]

'''


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def msort(arr):
            if len(arr)<=1: return arr
            mid = len(arr)//2
            l = msort(arr[:mid])
            r = msort(arr[mid:])

            nArr=[]
            lptr = 0
            rptr=0
            while lptr < len(l) or rptr < len(r):
                litem = l[lptr] if lptr < len(l) else None
                ritem = r[rptr] if rptr < len(r) else None

                if litem is not None and ritem is not None:
                    if litem < ritem:
                        nArr.append(litem)
                        lptr+=1
                    else:
                        nArr.append(ritem)
                        rptr+=1
                else:
                    if litem is not None:
                        nArr.append(litem)
                        lptr+=1
                    elif ritem is not None:
                        nArr.append(ritem)
                        rptr+=1
            return nArr

        return msort(nums)
        