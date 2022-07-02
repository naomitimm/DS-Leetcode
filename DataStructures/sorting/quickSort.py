def swap(l, x, y):
    (l[x], l[y]) = (l[y], l[x])

def quickSort(l, first, last):
    pivot = l[last]
    leftPointer = first
    rightPointer = last

    if first >= last:
        return l
    while leftPointer < rightPointer:
        while l[leftPointer] <= pivot and leftPointer < rightPointer:
            leftPointer += 1
        while l[rightPointer] >= pivot and leftPointer < rightPointer:
            rightPointer -= 1
        
        swap(l, leftPointer, rightPointer)
    swap(l, leftPointer, last)

    quickSort(l, first, leftPointer - 1)
    quickSort(l, leftPointer + 1, last)

    return l

l = [534,246,933, 127,277,321,454,565,2201]

print(quickSort(l, 0, len(l) -1 ))
