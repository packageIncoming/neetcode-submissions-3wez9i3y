class Solution:
    def binarySearch(self,row: List[int], target:int)-> bool:
        '''Helper function to perform binary search on the row that contains target'''
        # handle edge case where the row is empty (no valid row found)
        if len(row) == 0: return False
        # perform regular binary search here
        l,r = 0, len(row)-1
        while l <= r:
            mid = (l+r)//2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid +1
            elif row[mid] > target:
                r = mid-1
        return False

    def findRow(self, matrix: List[List[int]], target:int )-> List[int]:
        '''Helper function to find the row whose range contains target'''
        l,r = 0, len(matrix)-1
        while l<= r:
            mid = (l+r)//2
            mid_row = matrix[mid]
            if target < mid_row[0]: # target is below the middle row
                r=mid-1
            elif target > mid_row[-1]: # target is above the middle row
                l=mid+1
            else: #target >= mid_row[0] and target<= mid_row[-1], meaning target in range
                return mid_row
        return []

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.binarySearch(self.findRow(matrix,target),target)