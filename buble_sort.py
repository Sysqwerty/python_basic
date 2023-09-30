def buble_sort(array):
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

l = [1, 54, 0, -3, 14, -12]

print(buble_sort(l))