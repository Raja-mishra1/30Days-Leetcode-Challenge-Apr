class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        u = len(nums)-1
        while l<u:
            m = (l+u)//2
            if nums[m]>target:
                l = m
                return nums.index(i)
        return -1