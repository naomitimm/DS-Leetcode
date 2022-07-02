
def isValid(input):
    stack = []
    closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

    for char in input:
        if char is closeToOpen:
            if stack and stack[-1] == closeToOpen[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    
    if not stack: return True
    return False
    