class MinStack:

    def __init__(self):
        self.stack = []
        self.minValStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = min(val, self.minValStack[-1] if self.minValStack else val)
        self.minValStack.append(minVal)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minValStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minValStack[-1]