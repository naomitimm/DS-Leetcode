def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def siftDown(lst, i, upper):
    right, left = i*2 + 1, i*2 + 2

    while(True):
        # both children exist
        if max(right, left) < upper:
            if lst[i] >= max(lst[right], lst[left]):
                break
            elif lst[right] > lst[left]:
                swap(lst, i, right)
                i = right
            elif lst[left] > lst[right]:
                swap(lst, i, left)
                i = left
        # only 1 child exists 
        elif right < upper:
            if lst[i] < lst[right]:
                swap(lst, i, right)
                i = right
            break
        elif left < upper:
            if lst[i] < left:
                swap(lst, i, left)
                i = left
            break

        break

     

def main(lst):
    for element in range((len(lst) - 2) // 2, -1, -1):
    # len(lst) - 2 // 2 - because we neglect the leaf nodes
    # those that dont have children of their own
        siftDown(lst, element, len(lst))
    # this is the heapify part 
        print(lst)

    for end in range(len(lst) - 1, 0, -1):
        swap(lst, 0, end)
        siftDown(lst, 0, end)

    print(lst)

main([5, 16, 8, 14, 20, 1, 26])

