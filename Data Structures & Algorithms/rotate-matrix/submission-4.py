class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # reverse matrix vertically
        n=len(matrix[0])
        for r in range(n//2):
            matrix[r],matrix[n-r-1] = matrix[n-r-1],matrix[r]
        # swap column w row
        i=0
        while i < n:
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            i+=1
        print(matrix)