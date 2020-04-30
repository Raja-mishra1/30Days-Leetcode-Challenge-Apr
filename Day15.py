class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        ans = []
        for i in range(len(nums)): 
            ans.append(prod)
            prod *= nums[i]
        prod = 1
        for i in range(len(nums)-1, -1, -1): 
            ans[i] *= prod
            prod *= nums[i]
            
        return a