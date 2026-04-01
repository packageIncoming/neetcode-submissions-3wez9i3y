class Solution:

    def findRow(self, matrix, target):
        l, r= 0 , len(matrix)-1
        while l <= r:
            mid = (l+r)//2
            midRow = matrix[mid]
            if target >= midRow[0] and target <= midRow[-1]:
                return midRow
            elif target < midRow[0]:
                r=mid-1
            elif target > midRow[-1]:
                l=mid+1
    def binarySearch(self,row,target):
        if not row: return False
        l, r = 0, len(row)-1
        while l <= r:
            mid = (l+r)//2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l=mid+1
            elif row[mid] > target:
                r = mid-1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.binarySearch(self.findRow(matrix,target),target)