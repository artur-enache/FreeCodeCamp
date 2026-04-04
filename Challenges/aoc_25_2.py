import pytest
"""Advent of Code 2025, Day 2"""
# PART 1
# for elem in input_values:
#     boundary = elem.split('-')
#     begin = int(boundary[0])
#     end = int(boundary[1])
#
#     for num in range(begin, end + 1):
#         num_to_str = str(num)
#         if len(num_to_str) % 2 == 0:
#             middle = int(len(num_to_str)/2)
#             substring = num_to_str[0:middle]
#             if str(num).count(substring) == 2:
#                 sum += num

# PART 2
def process_id(number: int) -> int:
    to_string = str(number)
    length = len(to_string)
    max_digits_in_a_block = length // 2
    for digits_in_block in range(1, max_digits_in_a_block + 1):
        for num_of_digit_blocks in range(1, (length // digits_in_block) + 1):
            repunit = (10 ** (digits_in_block * num_of_digit_blocks) - 1) // (10 ** digits_in_block - 1)
            if int(to_string[0:digits_in_block]) * repunit == number:
                return number
            else:
                pass

def find_invalid_ids(values: tuple) -> list[int]:
    input_values = values.split(',')
    output_values = []
    for elem in input_values:
        boundary = elem.split('-')
        begin = int(boundary[0])
        end = int(boundary[1])

        for num in range(begin, end + 1):
            result = process_id(num)
            if result:
                output_values.append(result)
    return output_values

# Test cases
test1 = ('11-22') # 11, 22
test2 = ('95-115') # 99, 111
test3 = ('998-1012') # 999, 1010
test4 = ('1188511880-1188511890') # 1188511885
test5 = ('222220-222224') # 222222 (222220, 222221, 222222, 222223, 222224)
test6 = ('1698522-1698528') # None
test7 = ('446443-446449') # 446446
test8 = ('38593856-38593862') # 38593859
test9 = ('565653-565659') # 565656
test10 = ('824824821-824824827') # 824824824
test11 = ('2121212118-2121212124') # 2121212121

def test_no_1():
    assert find_invalid_ids(test1) == [11, 22]

def test_no_2():
    assert find_invalid_ids(test2) == [99, 111]

def test_no_3():
    assert find_invalid_ids(test3) == [999, 1010]

def test_no_4():
    assert find_invalid_ids(test4) == [1188511885]

def test_no_5():
    assert find_invalid_ids(test5) == [222222]

def test_no_6():
    assert find_invalid_ids(test6) == []

def test_no_7():
    assert find_invalid_ids(test7) == [446446]

def test_no_8():
    assert find_invalid_ids(test8) == [38593859]

def test_no_9():
    assert find_invalid_ids(test9) == [565656]

def test_no_10():
    assert find_invalid_ids(test10) == [824824824]

def test_no_11():
    assert find_invalid_ids(test11) == [2121212121]