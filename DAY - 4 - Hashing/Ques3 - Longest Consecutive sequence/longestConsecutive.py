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