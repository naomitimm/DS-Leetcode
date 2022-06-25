
class Stack:
    def __init__(self, items = []):
        self.elements = []
        self.stack = items

    def isEmpty(self):
        return len(self.elements) == 0

    def peek(self):
        if (self.isEmpty()):
            return None
        else:
            return self.elements[-1]

    def push(self, value):
        self.elements.append(value)

    def pop(self):
        if(self.isEmpty()):
            return None

        else:
            return self.elements.pop()

    def getSize(self):
        return len(self.elements)

    def __repr__(self):
        return "stack{0}".format(self.stack)



def reverse(stack):
    def reverseRecurssive(stack, newStack = Stack()):
        if(not stack.isEmpty()):
            newStack.push(stack.pop())
            reverseRecurssive(stack, newStack)
        return newStack
    return reverseRecurssive(stack)

stk = Stack(range(10))

print(stk)
print(reverse(stk))

def isPal(s):
    stack = Stack()

    for char in s:
        stack.push(char)
    
    for char in s:
        if char == stack.pop():
            return True
        
        return False
    
print(isPal("hello"))

