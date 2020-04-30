class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        N,M = binaryMatrix.dimensions()
        
        def find(row):
            left = 0
            right = M
            while left<right:
                middle = (left+right)//2
                if binaryMatrix.get(row,middle) == 0:
                    left = middle+1
                else:
                    right = middle
            return left
        
        best = M
        for row in range(N):
            column = find(row)
            best  = min(best,column)
        
        if best == M:
            return -1
        return best