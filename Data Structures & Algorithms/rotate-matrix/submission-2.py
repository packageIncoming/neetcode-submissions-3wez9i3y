class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # reverse matrix vertically
        matrix.reverse()
        # swap column w row
        i=0
        n=len(matrix[0])
        while i < n:
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            i+=1
        print(matrix)