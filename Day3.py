class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
         if len(nums) == 0:
            return 0
        
         csum = nums[0]
         max_sum = nums[0]
        
         for i in range(1, len(nums)):
                c_sum = nums[i] if csum < 0 else c_sum + nums[i]
                max_sum = max(c_sum, max_sum)
            
         return max_sum