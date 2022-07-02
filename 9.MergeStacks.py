from ..EXAM.stack1 import Stack

def MergeStack(stack1, stack2):
    newStack = Stack()

    a = stack1.pop()
    b = stack2.pop()

    while(stack1 and stack2):
        if a < b:
            newStack.push(a)
            a = stack1.pop()
        
        else:
            newStack.push(b)
            b = stack2.pop()
        
    while(stack1):
        newStack.push(stack1.pop())
    
    while(stack2):
        newStack.push(stack2.pop())


