# Method - 1 : Using extra space

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        
        for i in range(len(nums)):
            if(d.get(nums[i])):
                return nums[i]
            else:
                d[nums[i]] = 1
	return -1

# Method - 2 : Using Sorting

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        i=0
        j=1
        
        while(i<len(nums) and j<len(nums)):
            if(nums[i]==nums[j]):
                return nums[i]
            else:
                i+=1
                j+=1
        return -1

# Method - 3 : Only for 1 to n case

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            ind = abs(nums[i])
            
            if(nums[ind]<0):
                return ind
            else:
                nums[ind] = -nums[ind]
                
        return -1