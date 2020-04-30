class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       f = [x for x in nums if nums.count(x)==1]
       return f.pop()