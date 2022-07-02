def specialMin(tupleList):
    # return the minimum value and its index from its original list
    min, index = tupleList[0]

    for i in range(1, len(tupleList)):
        val, ind = tupleList[i]
        if(min < val):
            min = val; index = ind

    return (min, index)

def findMedian(list):
    if(len(list) == 3):
        # if len(list) == 3 median == the second minimum value
        list.remove(specialMin(list)) # remove the first min
        return specialMin(list)
            
    elif len(list) == 2:
        # if len(list) == 2 median = average
        return specialMin(list)

def quickSort(items):
    # base case
    if(len(items) <= 1):
        return items
    
    below_pivot = []
    above_pivot = []
    
    # since the min len(items) >= 2
    midSpace = [(items[0], 0),( items[-1], -1)] 
    if(len(items) > 2):
        mid = len(items) // 2
        midSpace.append((items[mid], mid))

    pivot, index = findMedian(midSpace)
    # remove the pivot
    # this prevent the infinite recursion in the case there are duplicate items e.g [8, 8] has 
    # median 8 hence below_pivot = [8, 8] which will create an infinite loop
    del items[index]

    for item in items:
        if item <= pivot:
            below_pivot.append(item)
        else:
            above_pivot.append(item)
    # doesn't include the pivot since the median could be outside the list
    return quickSort(below_pivot) + [pivot] + quickSort(above_pivot)

if __name__ == "__main__":
    l = [1, 8, 8, 9, 4, 4, 8, 7]

    print(quickSort(l))
