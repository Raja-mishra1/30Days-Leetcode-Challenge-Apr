class Solution:
    def countElements(self, arr: List[int]) -> int:
        c = 0
        dict = {}
        
        for i in arr:
            dict[i] = 1
            
        for j in arr:
            if j+1 in dict:
                c+=1
        return c