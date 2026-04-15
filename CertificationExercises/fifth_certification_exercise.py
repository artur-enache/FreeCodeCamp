"""
FreeCodeCamp, 5th certification exercise: Tower of Hanoi
https://www.freecodecamp.org/learn/python-v9/lab-tower-of-hanoi/implement-the-tower-of-hanoi-algorithm
"""
import pytest

def hanoi_solver(disks: int) -> str:
    a = [ i for i in range(disks, 0, -1) ]
    b = []
    c = []

    to_output = [f'{a} {b} {c}']

    def hanoi_mover(disks: int, source: list[int], buffer: list[int], target: list[int]):
        nonlocal to_output
        if disks == 0:
            return

        hanoi_mover(disks - 1, source, target, buffer)
        target.append(source.pop())
        to_output.append(f'{a} {b} {c}')
        hanoi_mover(disks - 1, buffer, source, target)

    hanoi_mover(disks, a, b, c)

    return '\n'.join(str(item) for item in to_output)

print(hanoi_solver(3))

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