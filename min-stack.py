# link: https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(value)
            self.min_stack.append(value)
            return

        current_min = min(value, self.getMin())
        self.min_stack.append(current_min)
        self.stack.append(value)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:

obj = MinStack()
obj.push(1)
obj.push(8)
obj.push(3)
obj.push(0)
obj.push(9)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()