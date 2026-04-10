"""
FreeCodeCamp, 5th certification exercise: Tower of Hanoi
https://www.freecodecamp.org/learn/python-v9/lab-tower-of-hanoi/implement-the-tower-of-hanoi-algorithm

Three rods, and a number of disks with different diameters.
At the start, all disks are on the first rod, in ascending order of diameters (biggest at bottom)

Move only the top disk
Move only one disk at a time
Cannot place larger disks on top of smaller disks

The function should solve the puzzle in (2**n) - 1 moves
The output is: the starting positions of disks on each rod, followed by the state of all rods after each move,
where the disks are represented by integers (1 is the smallest disk)

Example:
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]

I think that a way to phrase this problem is: I need to reach a state where the third list is empty, and the biggest
element of the first list is the only one in the list.

The third rod is the "target"
The rod with the next largest disk is the "source"
The remaining rod is the "buffer"

The starting state looks like this:
source buffer target

These rods need to update after each move. Ex. when n = 3:
S         B  T
[3, 2, 1] [] []

S      B   T
[3, 2] [] [1]

S    B  T
[3] [2] [1]

S   B      T
[3] [2, 1] []

B  S      T
[] [2, 1] [3]

B   S   T
[1] [2] [3]

S   B  T
[1] [] [3, 2]

-  -  T
[] [] [3, 2, 1]

But why does the solution take (2**n) - 1 moves? I also notice that when n % 2 = 1, the first move is from
source to target; while when n % 2 = 0, the first move is from source to buffer


"""
import pytest

def hanoi_solver(disks: int) -> str:
    pass

def test_1():
    assert hanoi_solver(2) == ('[2, 1] [] []\n'
                               '[2] [1] []\n'
                               '[] [1] [2]\n'
                               '[] [] [2, 1]')

def test_2():
    assert hanoi_solver(3) == ('[3, 2, 1] [] []\n'
                               '[3, 2] [] [1]\n'
                               '[3] [2] [1]\n'
                               '[3] [2, 1] []\n'
                               '[] [2, 1] [3]\n'
                               '[1] [2] [3]\n'
                               '[1] [] [3, 2]\n'
                               '[] [] [3, 2, 1]')

def test_3():
    assert hanoi_solver(4) == ('[4, 3, 2, 1] [] []\n'
                               '[4, 3, 2] [1] []\n'
                               '[4, 3] [1] [2]\n'
                               '[4, 3] [] [2, 1]\n'
                               '[4] [3] [2, 1]\n'
                               '[4, 1] [3] [2]\n'
                               '[4, 1] [3, 2] []\n'
                               '[4] [3, 2, 1] []\n'
                               '[] [3, 2, 1] [4]\n'
                               '[] [3, 2] [4, 1]\n'
                               '[2] [3] [4, 1]\n'
                               '[2, 1] [3] [4]\n'
                               '[2, 1] [] [4, 3]\n'
                               '[2] [1] [4, 3]\n'
                               '[] [1] [4, 3, 2]\n'
                               '[] [] [4, 3, 2, 1]')

def test_4():
    assert hanoi_solver(5) == ('[5, 4, 3, 2, 1] [] []\n'
                               '[5, 4, 3, 2] [] [1]\n'
                               '[5, 4, 3] [2] [1]\n'
                               '[5, 4, 3] [2, 1] []\n'
                               '[5, 4] [2, 1] [3]\n'
                               '[5, 4, 1] [2] [3]\n'
                               '[5, 4, 1] [] [3, 2]\n'
                               '[5, 4] [] [3, 2, 1]\n'
                               '[5] [4] [3, 2, 1]\n'
                               '[5] [4, 1] [3, 2]\n'
                               '[5, 2] [4, 1] [3]\n'
                               '[5, 2, 1] [4] [3]\n'
                               '[5, 2, 1] [4, 3] []\n'
                               '[5, 2] [4, 3] [1]\n'
                               '[5] [4, 3, 2] [1]\n'
                               '[5] [4, 3, 2, 1] []\n'
                               '[] [4, 3, 2, 1] [5]\n'
                               '[1] [4, 3, 2] [5]\n'
                               '[1] [4, 3] [5, 2]\n'
                               '[] [4, 3] [5, 2, 1]\n'
                               '[3] [4] [5, 2, 1]\n'
                               '[3] [4, 1] [5, 2]\n'
                               '[3, 2] [4, 1] [5]\n'
                               '[3, 2, 1] [4] [5]\n'
                               '[3, 2, 1] [] [5, 4]\n'
                               '[3, 2] [] [5, 4, 1]\n'
                               '[3] [2] [5, 4, 1]\n'
                               '[3] [2, 1] [5, 4]\n'
                               '[] [2, 1] [5, 4, 3]\n'
                               '[1] [2] [5, 4, 3]\n'
                               '[1] [] [5, 4, 3, 2]\n'
                               '[] [] [5, 4, 3, 2, 1]')