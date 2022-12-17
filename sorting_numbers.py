

def smallest(arr):
    smallest = arr[0]
    smallest_idx = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i
    return smallest_idx

def sort_items(arr):
    result=[]
    for i in range(0,len(arr)):
        smallest_num = smallest(arr)
        result.append(arr.pop(smallest_num))
    return result

my_list = [1,5,2,7,3,8,6,9,9]
print(sort_items(my_list))