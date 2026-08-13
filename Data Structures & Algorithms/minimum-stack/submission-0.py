class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.minimum) == 0 or value < self.minimum[-1]:
            self.minimum.append(value)
        else:
            self.minimum.append(self.minimum[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()