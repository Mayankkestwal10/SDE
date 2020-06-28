class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, arr, k):
        n = len(arr)
        mydict = dict() 
  
        sum = 0
        maxLen = 0
  
        for i in range(n): 

            sum += arr[i] 
  
     
            if (sum == k): 
                maxLen = i + 1
  
        
            elif (sum - k) in mydict: 
                maxLen = max(maxLen, i - mydict[sum - k]) 
  
            if sum not in mydict: 
                mydict[sum] = i 
  
        if(maxLen==0):
            return -1
            
        return maxLen 

        
