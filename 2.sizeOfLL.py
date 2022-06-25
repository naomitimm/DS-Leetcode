
class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def getSize(self):
        current = self.head
        count = 0

        while(current):
            count += 1
            current = current.nextNode
        return count
