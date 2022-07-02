from ..EXAM.stack1 import Stack

class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.minStack = Stack()

    def push(self, value: int) -> None:
        self.stack.push(value)

        # its a little tricky for min stack

        if self.minStack:
            value = min(value, self.minStack.pop())

        value = min(value, value)

        self.minStack.push(value)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack.pop()

    def getMin(self) -> int:
        return self.minStack.pop()