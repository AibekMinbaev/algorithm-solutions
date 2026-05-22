class MinStack:

    def __init__(self):
        self.stack: List[Tuple[int, int]]= []

    def push(self, val: int) -> None: 
        pair = (val, val)
        if self.stack: 
            last_val, last_min = self.stack[-1] 
            pair = (val, min(last_min, val))
        self.stack.append(pair) 

    def pop(self) -> None: 
        self.stack.pop() 

    def top(self) -> int: 
        last_val, last_min = self.stack[-1]
        return last_val

    def getMin(self) -> int: 
        last_val, last_min = self.stack[-1]
        return last_min
    