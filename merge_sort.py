def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array
    if len(array) == 2:
        return array if array[0] < array[1] else [array[1], array[0]]
    middle_array = int(len(array) / 2)
    left_part = array[0:middle_array]
    right_part = array[middle_array:len(array)]
    sorted_left_part = merge_sort(left_part)
    sorted_right_part = merge_sort(right_part)
    i = 0
    j = 0
    new_sorted_array = []
    while len(sorted_left_part) != i and len(sorted_right_part) != j:
        if sorted_left_part[i] < sorted_right_part[j]:
            new_sorted_array.append(sorted_left_part[i])
            i += 1
        else:
            new_sorted_array.append(sorted_right_part[j])
            j += 1
    if i < len(sorted_left_part):
        new_sorted_array += sorted_left_part[i:len(sorted_left_part)]
    else:
        new_sorted_array += sorted_right_part[j:len(sorted_right_part)]


    return new_sorted_array


def main():
    array = [5, 4, 5, 6, 7, 2, 1, 4, 5, 6, 7, 4, 3, 2, 43, 5, 76, 78, 89, 9]
    print(merge_sort(array))


main()