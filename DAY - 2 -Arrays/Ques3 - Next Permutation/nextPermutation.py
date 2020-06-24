class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        inverse_point = len(nums) - 2
        
        while(inverse_point>=0 and nums[inverse_point]>=nums[inverse_point+1]):
            inverse_point-=1
        
        if(inverse_point<0):
            return nums.reverse()
        
        for i in reversed(range(inverse_point, len(nums))):
            if(nums[i]>nums[inverse_point]):
                nums[i], nums[inverse_point] = nums[inverse_point], nums[i]
                break
        
        nums[inverse_point+1:] = reversed(nums[inverse_point+1:])
        
        return nums
        