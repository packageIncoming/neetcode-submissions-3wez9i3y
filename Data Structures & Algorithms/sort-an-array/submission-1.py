class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,l,m,r):
            left = arr[l:m+1]
            right = arr[m+1:r+1]
            arrPtr,lPtr,rPtr=l,0,0

            while lPtr < len(left) and rPtr < len(right):
                if left[lPtr] < right[rPtr]:
                    arr[arrPtr] = left[lPtr]
                    arrPtr+=1
                    lPtr+=1
                else:
                    arr[arrPtr] = right[rPtr]
                    arrPtr+=1
                    rPtr+=1
            
            while lPtr < len(left):
                arr[arrPtr] = left[lPtr]
                arrPtr+=1
                lPtr+=1
            while rPtr < len(right):
                arr[arrPtr] = right[rPtr]
                arrPtr+=1
                rPtr+=1

        def mergeSort(l,r):
            if l >= r:
                return # already sorted, len<=1
            m=(l+r)//2
            mergeSort(l,m)
            mergeSort(m+1,r)
            merge(nums,l,m,r)
        
        mergeSort(0,len(nums)-1)
        return nums