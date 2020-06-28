class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for i, j in enumerate(nums):
            d[j] = i
            
        for i in range(len(nums)):
            rem = target - nums[i]
            if(d.get(rem) and i!=d[rem]):
                return [i, d[rem]]
        