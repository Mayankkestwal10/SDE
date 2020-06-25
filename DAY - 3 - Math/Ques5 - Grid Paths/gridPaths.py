# Method - 1 - DP solution

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        t = [[1 for j in range(n)] for i in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                t[i][j] = t[i-1][j]+t[i][j-1]
                
        return t[m-1][n-1]

# Method - 2
/*
Delannoy Number
In mathematics, a Delannoy number D describes the number of paths from the southwest corner (0, 0) of a rectangular grid to the northeast corner (m, n), using only single steps north, northeast, or east.

(m+n-2)! / ( (m-1)! * (n-1)! )
*/

import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))