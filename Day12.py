import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones) - 1):
            stones.sort()
            temp=stones[-1] - stones[-2]
            stones[-2]=-1
            stones[-1]=temp
        return (stones[-1])