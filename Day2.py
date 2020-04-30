class Solution:
    def isHappy(self, n: int) -> bool:
        n_s = set()
        sqr = 0  
        while sqr != 1:
            sqr = 0  
            while n > 0: 
                sqr += (n % 10) ** 2
                n = n // 10
				
            if sqr == 1: return True
			
            elif sqr in n_s: return False
            else: 
                n = sqr       
                n_s.add(n)
        