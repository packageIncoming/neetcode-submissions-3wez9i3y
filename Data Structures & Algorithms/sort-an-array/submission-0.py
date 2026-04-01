class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divideAndConquer(arr):
            if len(arr) <= 1:
                return arr # already 'sorted' since 1 element
            halfIdx = (len(arr))//2
            left = divideAndConquer(arr[:halfIdx])
            right= divideAndConquer(arr[halfIdx:])

            sArr = []

            lPtr=0
            rPtr=0

            while lPtr < len(left) and rPtr < len(right):
                if left[lPtr] < right[rPtr]:
                    sArr.append(left[lPtr])
                    lPtr+=1
                else:
                    sArr.append(right[rPtr])
                    rPtr+=1
            
            while lPtr < len(left):
                sArr.append(left[lPtr])
                lPtr+=1
            while rPtr < len(right):
                sArr.append(right[rPtr])
                rPtr+=1

            return sArr
        
        return divideAndConquer(nums)