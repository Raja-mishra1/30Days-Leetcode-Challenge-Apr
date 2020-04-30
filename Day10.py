class MinStack:
    def __init__(self):
        self.stack = []
        self.minVal = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minVal:
            val,count = self.minVal[-1] 
            if val>x:
                self.minVal.append((x,1))
            elif val==x:
                self.minVal[-1] = (val,count+1)
        else:
            self.minVal.append((x,1))
            
    def pop(self) -> None:
        val,count = self.minVal[-1]
        if val==self.stack[-1]:
            count -=1
            if count == 0 : self.minVal.pop()
            else : self.minVal[-1] = (val,count)
        return self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        val,count = self.minVal[-1]
        return val