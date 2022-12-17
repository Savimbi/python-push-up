

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        less = [i for i in arr[1:] if i<= pivot]
        greater = [i for i in arr[1:] if i> pivot]

        return quick_sort(less)+[pivot]+quick_sort(greater)

my_list = [4,5,2,4,7,4,5,9,7,8,2]
print(quick_sort(my_list))

