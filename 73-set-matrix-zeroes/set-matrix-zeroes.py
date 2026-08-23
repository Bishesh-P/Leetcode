class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rows = [False] * m
        column = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows[i] = True
                    column[j] = True
                
        for i in range(m):
            for j in range(n):
                if rows[i] or column[j]:
                    matrix[i][j] = 0
        
        