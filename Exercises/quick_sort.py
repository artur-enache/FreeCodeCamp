# Work in progress
def quick_sort(input_list: list[int]) -> list[int]:
    if len(input_list) <= 1:
        return []

    output_list = []
    pivot = input_list[0]
    print('pivot: ', pivot)

    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []

    for item in input_list:
        if item < pivot:
            less_than_pivot.append(item)
        elif item == pivot:
            equal_to_pivot.append(item)
        else:
            greater_than_pivot.append(item)

    less_than_pivot = quick_sort(less_than_pivot)
    equal_to_pivot = quick_sort(equal_to_pivot)
    greater_than_pivot = quick_sort(greater_than_pivot)

    output_list.extend(less_than_pivot)
    print('1: ', output_list)
    output_list.extend(equal_to_pivot)
    print('2: ', output_list)
    output_list.extend(greater_than_pivot)
    print('3: ', output_list)
    print('output: ', output_list)

    return output_list

quick_sort([20, 3, 14, 1, 5])