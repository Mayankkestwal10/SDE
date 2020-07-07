# Method - 1  O(nlogn)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums = sorted(nums)
        
        print(nums)
        
        n = len(nums)
        cnt = 1
        ans = 0
        for i in range(1, n):
            if(nums[i]==nums[i-1]+1):
                cnt+=1
            else:
                ans = max(cnt, ans)
                cnt = 1
                
        return ans


# Method - 2 Time Complexity - O(n^2)      
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        
        ans, val = 0, 0
        
        for x in nums:
            if x-1 not in nums:
                val = 0
                while x in nums:
                    val = val+1
                    x = x+1
                    
            ans = max(ans, val)
        
        return ans


# Method - 3 (Streak) - O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        
        if(n==0):
            return 0
        if(n==1):
            return 1
        
        for i in range(n):
            r = 0
            l = 0
            
            if(nums[i] not in d.keys()):
                if(nums[i]-1 in d):
                    l = d[nums[i]-1]
                
                if(nums[i]+1 in d):
                    r = d[nums[i]+1]
            else:
                continue
           
            d[nums[i]] = l+r+1
                
            d[nums[i]-l] = l+r+1
            
            d[nums[i]+r] = l+r+1
                
                

        return max(d.values())