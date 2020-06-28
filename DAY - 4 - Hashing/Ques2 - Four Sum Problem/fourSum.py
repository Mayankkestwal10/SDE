# Method - 1 - Sorting + O(n^3)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        
        
        nums = sorted(nums)
        
        res = []
        
        for i in range(n-3):
            for j in range(i+1, n-2):
                l = j+1
                r = n-1
                
                while(l<r):
                    if(nums[i]+nums[j]+nums[l]+nums[r]==target):
                        res.append((nums[i], nums[j], nums[l], nums[r]))
                        l+=1
                        r-=1
                    elif(nums[i]+nums[j]+nums[l]+nums[r]<target):
                        l+=1
                    else:
                        r-=1
        
        res = tuple(res)
        return set(res)