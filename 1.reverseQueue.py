from .DataStructures.queue_optimal import Queue
from .DataStructures.stack1 import Stack

queue = Queue()
for i in range(10):
    queue.enqueue(i)

stack = Stack()

while(not queue.isEmpty()):
    for i in range(queue.getSize()):
        stack.push(queue.dequeue())
    
while(not stack.isEmpty()):
    for i in range(stack.getSize()):
        queue.enqueue(stack.pop())
        