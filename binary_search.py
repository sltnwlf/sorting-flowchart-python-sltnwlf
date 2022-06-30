# Binary Search algorithm
array = [1, 2, 4, 7, 11, 22, 38, 42, 43]  # list to index search


def my_search(array, item, start, end):

    if end - start == 1:
        if array[start] == item:
            return start
        else:
            return -1
    mid = int((end - start) / 2)
    if array[start + mid] > item:
        return my_search(array, item, start, end - mid)
    else:
        return my_search(array, item, start + mid, end)


def my_binary_search(array, item):

    item = int(input("Enter a value: "))
    return my_search(array, item, 0, len(array))


print("Index of searched value: " + str(my_binary_search(array, 'index')))
