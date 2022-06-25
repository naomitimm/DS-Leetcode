from DataStructures.linkedList_optimal import Linkedlist

class Queue:
    def __init__(self):
        self.elements = Linkedlist()

    def enqueue(self, data):
        self.elements.addLast(data)
    
    def dequeue(self):
        if(self.elements.isEmpty()):
            return None
        else:
            return self.elements.removeNode(0)
           
    
    def getSize(self):
        return self.elements.size()
    
    def isEmpty(self):
        return self.elements.isEmpty()

    def __str__(self):
        return self.elements.__str__()


def isPal(word):
    q = Queue()

    for char in word:
        q.enqueue(char)
    
    while(len(word) > 0):
        if(word[-1] == q.dequeue()):
            word = word[:-1]
        else:
            break
        

    if(len(word) == 0):
        return True
    return False

print(isPal("level"))

