def MergeSort(array):
    if len(array) == 1:
        return merge(array, [])
    mid = int(len(array) / 2)
    left = array[:mid]
    right = array[mid:]
    return merge(MergeSort(left), MergeSort(right))


def merge(left, right):
    i = 0
    j = 0
    result = []
    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if j == len(right):
        result.extend(left[i:])
    if i == len(left):
        result.extend(right[j:])
    return result


def test():
    array = [12,13,29,76,83,55,47,89,51,62,37,44,9,56,83,79]
    print(MergeSort(array))


test()
