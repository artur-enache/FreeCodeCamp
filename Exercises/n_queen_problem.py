"""https://www.freecodecamp.org/learn/python-v9/lab-n-queens-problem/implement-the-n-queens-algorithm

Problem: place N Queens on an NxN board, so that no two queens attack each other
This means that no two Queens share a row, column or diagonal

When n = 4 a valid arrangement is [1, 3, 0, 2]
In row 0, Q is in column 1
In row 1, Q is in column 3
In row 2, Q is in column 0
In row 3, Q is in column 2

Must be implemented using a "DFS approach"

Input: n, which represents the # of Queens to place, and also the matrix dimensions
Output: a list of solutions (valid arrangement), where each list is of length n, and where the list element at index i
is the column index (0-based) of the queen in row i

How to transform the input into the output:
"""
import pytest

def dfs_n_queens(queens: int) -> list[list[int]]:
    if queens < 1:
        return []

def test_1():
    assert dfs_n_queens(1) == [[0]]

def test_2():
    assert dfs_n_queens(2) == []

def test_3():
    assert dfs_n_queens(3) == []

def test_4():
    assert dfs_n_queens(4) == [[1, 3, 0, 2], [2, 0, 3, 1]]

def test_5():
    assert dfs_n_queens(5) == [[0, 2, 4, 1, 3], [0, 3, 1, 4, 2], [1, 3, 0, 2, 4], [1, 4, 2, 0, 3], [2, 0, 3, 1, 4],
                               [2, 4, 1, 3, 0], [3, 0, 2, 4, 1], [3, 1, 4, 2, 0], [4, 1, 3, 0, 2], [4, 2, 0, 3, 1]]

def test_6():
    assert len(dfs_n_queens(5)) == 10

def test_7():
    assert len(dfs_n_queens(8)) == 92