import pytest
"""Advent of Code 2025, Day 1"""

# PART 1
# result = 0
# dial = 50
#
# def calculate_operation(line: str):
#     return int(line[1:]) if line[0] == 'R' else int(line[1:]) * -1
#
# with open('aoc_25_1_input.txt') as input_file:
#     for line in input_file:
#         operation = calculate_operation(line)
#         dial += operation
#         if dial % 100 == 0 or dial == 0:
#             result += 1
#     print(result)

# PART 2
small_values = [ 'L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82' ] # passes 3 times, and lands 3 times
large_values = [ 'R1000' ] # passes 10 times
large_mixed_values = [ 'R1000', 'L600' ] # passes 16
large_mixed_and_zero_values = [ 'R1000', 'L600', 'R50' ] # passes 16, lands 1

def calculate_operation(line: str):
    return int(line[1:]) if line[0] == 'R' else int(line[1:]) * -1

def turn_dial(value_list: list) -> int:
    global dial
    global result
    result = 0
    dial = 50
    for item in value_list:
        pass
    return result

def test_small_values():
    assert turn_dial(small_values) == 6

def test_one_large_value():
    assert turn_dial(large_values) == 10

def test_large_mixed_values():
    assert turn_dial(large_mixed_values) == 16

def test_large_and_zero_values():
    assert turn_dial(large_mixed_and_zero_values) == 17

#
# with open('aoc_25_1_input.txt') as input_file:
#     for line in input_file:
#         turn_dial(line)
#     print(result)