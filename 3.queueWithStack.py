from .DataStructures.stack1 import Stack

class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, data):
        if (self.s1.isEmpty() and self.s2.isEmpty()):
            self.s1.push(data)
        
        elif (not self.s2.isEmpty()):
            while(self.s2.getSize() > 0):
                self.s1.push(self.s2.pop())
            self.s1.push(data)
        
    
    def dequeue(self):
        if(self.s2.isEmpty() and not self.s1.isEmpty()):
            while(self.s1.getSize() > 0):
                self.s2.push(self.s1.pop())
            return self.s2.pop()
        return self.s2.pop()

    
    def getSize(self):
        return self.s1.getSize() + self.s2.getSize()

