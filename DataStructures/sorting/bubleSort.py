list1 = [1, 2, 4, 3, 7, 0]
for i in range(5):
    for element in range(5):
        if list1[element] > list1[element + 1]:
            temp = list1[element]
            list1[element] = list1[element + 1]
            list1[element + 1] = temp
    #     print(l, "inner loop")
    # print(l, "OUTER")
print(list1)

# improved
def bubleSort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j] = l[j] + l[j + 1]
                l[j + 1] = l[j] - l[j + 1]
                l[j] = l[j] - l[j + 1]
    print(l)

bubleSort([1, 4, 7, 3, 55, 9])

# WORST-CASE TIME : O(n)^2
