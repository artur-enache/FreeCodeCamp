"""https://www.freecodecamp.org/learn/python-v9/lab-nth-fibonacci-number/build-an-nth-fibonacci-number-calculator

0, 1, 1, 2, 3, 5, 8, 13

N-th numbers:
0 = 0
1 = 1
2 = 1
3 = 2
4 = 5
5 = 8
"""

import pytest

# This is a good solution, but does not respect one of the requirements of the exercise:
# "Each computed number at the position n in the Fibonacci sequence should be stored
# in the sequence list at index n - 1."
def fibonacci(n: int) -> int:
    sequence = [0, 1]
    if n <= 1:
        return sequence[n]

    while len(sequence) <= n:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence[-1]

def test_1():
    assert fibonacci(0) == 0

def test_2():
    assert fibonacci(1) == 1

def test_3():
    assert fibonacci(2) == 1

def test_4():
    assert fibonacci(3) == 2

def test_5():
    assert fibonacci(5) == 5

def test_6():
    assert fibonacci(10) == 55

def test_7():
    assert fibonacci(15) == 610