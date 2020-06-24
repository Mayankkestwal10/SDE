# Method 1 - With Extra Space

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        d = []
        n = len(matrix)
        
        for i in zip(*matrix):
            d.append(list(i)[::-1])
        
        for i in range(n):
            matrix[i] = d[i]
        

# Method 2 - Without Extra Space (Using Transpose)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in range(n):
            matrix[i] = matrix[i][::-1]