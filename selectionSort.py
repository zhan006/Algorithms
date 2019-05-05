def selectionSort(array):
    for i in range(len(array)-1):
        minimum = i
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                minimum = j
        v=array[i]
        array[i]=array[minimum]
        array[minimum]=v
    return array


def test():
    array = [7, 6, 5, 4, 3, 2, 1]
    array = selectionSort(array)
    print(array)


if __name__ == "__main__":
    test()
