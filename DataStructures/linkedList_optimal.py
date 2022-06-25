
class Node:
    """an object for storing a single node in a liked list"""
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode


class Linkedlist:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while(current != None):
            # while current != None
            count += 1
            current = current.nextNode
        
        return count

    def addAtStart(self, data):
        newNode = Node(data)
        newNode.nextNode = self.head
        self.head = newNode

    def search(self, key):
        current = self.head

        while(current != None):
            if current.value == key:
                print("found")
                return current
            else:
                print("going to next one")
                current = current.nextNode
        return "Node not found in list"

    def insertAt(self, data, index):
        if index == 0:
            self.addAtStart(data)

        if index > 0:
            newNode = Node(data)
            position = index
            current = self.head
        
        while position > 1:
            current = newNode.nextNode
            position -= 1
        
        prevNode = current
        nextNode = current.nextNode

        prevNode.nextNode = newNode
        newNode.nextNode = nextNode
        

    def removeNode(self, key):
        current = self.head
        prev = None
        found = False

        while(current and not found):
            if current.value == key and current is self.head:
                found = True
                self.head = current.nextNode

            elif current.value == key:
                found = True
                prev.nextNode = current.nextNode
            
            else:
                prev = current
                current = current.nextNode

        return current

    def addLast(self, data):
        newNode = Node(data)

        listSize = self.size()

        if listSize == 0:
            self.head = self.tail = newNode
        
        else:
            self.tail.nextNode = newNode
            self.tail = self.tail.nextNode

    def removeFirst(self):
        if(self.isEmpty):
            return None
        else:
            temp = self.head
            self.head = self.head.nextNode
            temp.nextNode = None
            return temp.value

    def reverse(self):
        current = self.head
        prev = None

        while(current is not None):
            next = current.nextNode
            current.nextNode = prev
            prev = current
            current = next
        self.head = prev
    
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.value)
            temp = temp.nextNode

    
   


        



# ll = Linkedlist()
# ll.addAtStart(7)
# ll.addAtStart(34)
# ll.insertAt(45, 1)
# print(ll.size())

# print(ll.search(4))
# print('\n')
# print(ll.search(7))
# print('\n wait what')

# ll.removeNode(7)
# print('\n node 7 should be gone')
# print(ll.search(7))

# print(ll.search(45))



