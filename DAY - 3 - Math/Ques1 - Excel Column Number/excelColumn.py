import math
class Solution:
    def titleToNumber(self, s: str) -> int:
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        n = len(s)
        
        d = {}
        
        for i, j in enumerate(alpha):
            d[j] = i+1
            
        total = 0
        
        for i in range(n):
            total = total + math.pow(26, i)*d[s[n-i-1]]
            
            
        return int(total)