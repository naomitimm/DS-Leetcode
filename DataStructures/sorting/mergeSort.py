def mergeSort(l):
    if len(l) == 1:
        return l[0]
    
    middle = len(l) // 2
    leftHalf = l[:middle]
    rightHalf = l[middle:]

    mergeSort(leftHalf)
    mergeSort(rightHalf)

    i = j = k = 0
    #current index in left half, current index in right half, merged array index

    while len(leftHalf) > i and len(rightHalf) > j:
        if leftHalf[i] <= rightHalf[j]:
            l[k] = leftHalf[i]
            i += 1
        else:
            l[k] = rightHalf[j]
            j += 1
        k += 1

    while len(leftHalf) > i:
        l[k] = leftHalf[i]
        i += 1
        k += 1
    while len(rightHalf) > j:
        l[k] = rightHalf[j]
        j += 1
        k += 1

    return l

print(mergeSort([1]))