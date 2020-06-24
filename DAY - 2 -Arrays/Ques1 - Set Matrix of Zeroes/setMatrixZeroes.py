class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, col = len(matrix), len(matrix[0])
        
        n_row, n_col = set(), set()
        
        for i in range(rows):
            for j in range(col):
                if(matrix[i][j]==0):
                    n_row.add(i)
                    n_col.add(j)
                    
        for i in n_row:
            matrix[i] = [0]*col
            
        for i in range(rows):
            for j in n_col:
                matrix[i][j] = 0
        