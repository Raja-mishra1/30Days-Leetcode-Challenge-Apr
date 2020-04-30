class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for k in range(len(nums)):
            if nums[k]!=0:
                nums[k], nums[i] = nums[i], nums[k]
                i+=1