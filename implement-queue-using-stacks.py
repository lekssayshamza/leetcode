class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if not self.stack_out:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop(-1))

        return self.stack_out.pop()       
        

    def peek(self) -> int:
        if not self.stack_out:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop(-1))

        return self.stack_out[-1]
        

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)
        


q = MyQueue()

print(q.empty())

q.push(10)
q.push(20)
q.push(30)

print(q.empty())

print(q.peek())  # 10
print(q.peek())  # 10

print(q.empty())

print(q.pop())   # 10
print(q.peek())  # 20