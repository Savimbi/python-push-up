# O(n) time as we may pass through the whole array and O(1) space, as we are keep using the same array
def is_monotonic(array):
    is_non_decrease = True
    is_non_increase = True

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            is_non_increase = False
        if array[i] < array[i - 1]:
            is_non_decrease = False
    return is_non_decrease or is_non_increase
