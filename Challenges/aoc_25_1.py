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

"""
Part two: I need to count both the number of times:
- the dial lands on 0
- the dial passes 0

So, for example:
dial = 90
rotate R20
it lands on 10, but passes 0 once

I need to add one more else if clause, to check:
is 0 > operation + dial or 100 < operation + dial 

But this doesn't work for my current implementation, because I never "converted" the dial value to fall in a range of
0 - 99

Ok, then first, I need to modify the current implementation: set the dial = dial % 100 before doing any work

The else if clause I described above does not work; if the number is very large (ex. 5000) then my clause will
report that the dial passed 0 only once, not 50 times

Let's assume the rotation is R1000:
- if the dial is at 0, this rotation will pass 0 nine times, and the 10th time it also lands on 0 (should this be 
counted as both "passed" and "landed", or just "landed"?)
- if the dial is at 50, this rotation will pass 0 ten times
- if the dial is at 99, this rotation will pass 0 ten times

I think the exercise threw me a curveball, and I should not stick to my previous implementation: I now do not care at
all about the number of times the dial lands on 0, only how many times it passes 0.

Therefore, I need to understand how many times the dial + operation will cross the boundary of 0 - 99 for each input
So:
(dial + operation) // 100 = number of times it passed 0
(50 + 1000) // 100 = 10
(50 - 1000) // 100 = -10

But, as I've learned in the meantime, this does not apply for numbers small enough to make the dial cross 0 or 100 
only once. Also, after re-reading the exercise, I was wrong earlier: 
I do still care about the number of times the dial lands on 0.

I made another new mistake in my implementation, but I do not understand why it did not occur in the first part: when
spinning it enough to the left, the dial is never supposed to be ex. -1, but it should be 99 instead.

I think it did not matter because I was checking either for multiples of 100, or for 0. The dial -1 is mathematically 
equivalent to 99 (i.e. if I add 1 to both, they both end up on 0), and this has no bearing on the result of the check.
"""

