class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = 0
        n = len(A)
        xor = [0]*n
        
        d = {}
        
        xor[0] = A[0]
        
        for i in range(1, n):
            xor[i] = xor[i-1]^A[i]
            
        for i in range(n):
            temp = B^xor[i]
            
            if temp in d.keys():
                ans = ans+d[temp]
                
            if (xor[i]==B):
                ans+=1
                
            d[xor[i]] = d.get(xor[i], 0)+1
            
        return ans