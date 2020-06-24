# Time Complexity - O(n2)

class Solution:
    def countInv(self, A: List[int]) -> int:	
        globalInersions = 0
	for i in range(n):
    	    for j in range(i+1, n):
                if(A[i]>A[j]):
    		    globalInversions+=1
	
	return globalInversions