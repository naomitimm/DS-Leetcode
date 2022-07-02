from stack1 import Stack

#complexity == O(n)
def isPalindrom(str):
    stack = Stack()
    palindrom = False

    for char in str:
        stack.push(char)
    
    for char in str:
        if char == stack.pop():
            palindrom = True
        
        else:
            palindrom = False
    return palindrom

print(isPalindrom("level"))



