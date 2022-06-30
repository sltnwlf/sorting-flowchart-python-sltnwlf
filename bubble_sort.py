# Bubble Sort algorithm
array = [1, 2, 56, 32, 51, 2, 8, 92, 15]  # list to swap


def my_bubble_sort(list_to_swap):
    n = len(list_to_swap)
    i = 0

    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                j += 1
            else:
                j += 1
        i += 1
    print('Ordered list: ' + str(array))


my_bubble_sort(array)
