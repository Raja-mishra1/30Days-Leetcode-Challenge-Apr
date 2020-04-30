class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 0 or s== '*':
            return True
        if len(s) == 1:
            return False
        lb = 0
        for i in s:
            if i == ')':
                lb-=1
            else:
                lb+=1
            if lb < 0 :
                return False
        if lb == 0:
            return True
        rb = 0
        
        for i in reversed(s):
            if i =='(':
                rb -=1
            else:
                rb+=1
            if rb<0:
                return False
        return True
