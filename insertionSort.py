def insertionSort(array):
    for i in range(1, len(array)):
        v = array[i]
        j = i - 1
        while j >= 0 and array[j] > v:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = v
    return array


def shellSort(array, step):
    for i in range(step, len(array)):
        j = i - step
        v = array[i]
        while j >= 0 and array[j] > v:
            array[j + step] = array[j]
            j -= step
        array[j + step] = v
    return array


def test():
    array = [98, 14, 55, 31, 44, 83, 25, 77, 47, 57, 49, 52, 72, 29, 64, 26, 33, 89, 38, 32, 94, 17]
    # print(insertionSort(array))
    # print(array)
    print(shellSort(array, 1))


test()
