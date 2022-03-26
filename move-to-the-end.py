def move_element_to_end(original_array, to_move):
    start_idx = 0
    end_idx = len(original_array) - 1

    while start_idx < end_idx:
        while end_idx == to_move:
            end_idx -= 1
        if original_array[start_idx] == to_move:
            original_array[start_idx], original_array[end_idx] = original_array[end_idx], original_array[start_idx]
        start_idx += 1

    return original_array


toMove = 2
array = [2, 1, 2, 2, 2, 3, 1, 4, 2, 5]
print(move_element_to_end(array, toMove))
