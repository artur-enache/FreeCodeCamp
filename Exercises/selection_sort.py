import pytest

def selection_sort(input_list: list[int]) -> list[int]:
    if len(input_list) <= 1:
        return input_list
    else:
        length = len(input_list)

        for i in range(0, length):
            smallest_value_index = i

            for j in range(i+1, length):
                if input_list[j] < input_list[smallest_value_index]:
                    smallest_value_index = j

            if smallest_value_index != i:
                current_value = input_list[i]
                input_list[i] = input_list[smallest_value_index]
                input_list[smallest_value_index] = current_value

    return input_list

def test_1():
    assert selection_sort([33, 1, 89, 2, 67, 245]) == [1, 2, 33, 67, 89, 245]

def test_2():
    assert selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]) == [3, 5, 12, 15, 16, 23, 72, 99, 567]

def test_3():
    assert (selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]) ==
            [1, 1, 2, 2, 4, 8, 32, 43, 43, 55, 63, 92, 123, 123, 234, 345, 5643])