import pytest

def quick_sort(input_list: list[int]) -> list[int]:
    output_list = []

    if len(input_list) >= 1:
        pivot = input_list[0]
    else:
        pivot = None

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

    if len(less_than_pivot) > 1:
        less_than_pivot = quick_sort(less_than_pivot)

    if len(greater_than_pivot) > 1:
        greater_than_pivot = quick_sort(greater_than_pivot)

    output_list.extend(less_than_pivot)
    output_list.extend(equal_to_pivot)
    output_list.extend(greater_than_pivot)

    return output_list

def test_1():
    assert quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]) == [11, 11, 18, 18, 23, 23, 56, 56, 87, 87]

def test_2():
    assert quick_sort([4, 42, 16, 23, 15, 8]) == [4, 8, 15, 16, 23, 42]

def test_3():
    assert quick_sort([83, 4, 24, 2]) == [2, 4, 24, 83]

def test_4():
    assert quick_sort([20, 3, 14, 1, 5]) == [1, 3, 5, 14, 20]