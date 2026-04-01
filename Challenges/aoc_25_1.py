"""Advent of Code 2025, Day 1"""
"""
Circular dial, 0-99. Input contains lines with direction + value (left / right, int)
Ex: dial at 50 and input R51 means the dial spins right; when it reaches 99, it continues from 0; so in this case 
the dial lands on 1 (100 = 0, 101 = 1)

Goal: process each line, and determine how many times the dial lands on precisely 0 after any operation

The obvious solution: read each line, assign L to minus, R to plus. Add the value it to the current dial value, then
check if value == 100; in which case count 1 towards the solution then reset the value to 0.

But what happens if I add a large number (input > 100)?

operation = +/- input
if dial + operation > 99:
initial rotation = 100 - dial
elif dial + operation < 0:
initial rotation = dial

number of full rotations left = abs(initial rotation + operation) // 100 (but I don't care about full rotations)
remaining partial rotations  = abs(initial rotation + operation) % 100

Maybe I am overcomplicating things. What if I just:

read each line
if L: operation is negative
if R: operation is positive
On each line, check dial + operation % 100 == 0 or dial == 0
if yes, result += 1
repeat for each line

And that's it? Yes, that approach worked.
"""

result = 0
dial = 50

def calculate_operation(line: str):
    return int(line[1:]) if line[0] == 'R' else int(line[1:]) * -1

with open('aoc_25_1_input.txt') as input_file:
    for line in input_file:
        operation = calculate_operation(line)
        dial += operation
        if dial % 100 == 0 or dial == 0:
            result += 1
    print(result)