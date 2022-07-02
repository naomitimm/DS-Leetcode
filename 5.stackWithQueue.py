from ..EXAM.queue_optimal import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    
    def push(self, data):
        if(self.q1.isEmpty() and self.q2.isEmpty()):
            self.q1.enqueue(data)
        
        elif (not self.q2.isEmpty()):
            while(self.q2.getSize() > 0):
                self.q1.enqueue(self.q2.dequeue())
            self.q1.enqueue(data)
        
    def pop(self):
        if(not self.q1.isEmpty() and self.q2.isEmpty()):
            while(self.q1.getSize() > 1):
                self.q2.enqueue(self.q1.dequeue())
            return self.q2.dequeue()
        return self.q2.dequeue()

    def getSize(self):
        return self.q1
