
#searching the index of item in the list
def binary_search(list, item):
    low_idx = 0
    high_idx = len(list) -1

    while low_idx <= high_idx:

        mid_idx =low_idx + high_idx
        guess = list[mid_idx]

        if guess == item:
            return mid_idx
        if guess > item:
            high_idx = mid_idx - 1
        else:
            low_idx = mid_idx + 1
    return None

my_list = [4,2,6,4,5,8]
print(binary_search(my_list,5))

