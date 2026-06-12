class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]


    def push(self, val: int) -> None:
        if self.min_stack:
            if val<self.min_stack[-1]:
                min_value=val
            else:
                min_value=self.min_stack[-1]
        else:
                min_value=val
        self.min_stack.append(min_value)
        self.stack.append(val)
            

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] 

    def getMin(self) -> int:
        return self.min_stack[-1]
        
