"""https://www.freecodecamp.org/learn/python-v9/lab-depth-first-search/lab-depth-first-search"""

import pytest

def dfs(matrix: list[list[int]], node_label: int) -> list[int]:
    stack = []
    visited = set()

    stack.append(node_label)
    while stack:
        node = stack.pop()
        visited.add(node)

        for index, edge in enumerate(matrix[node]):
            if edge and index not in visited:
                stack.append(index)

    return sorted(visited)

def test_1():
    assert dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1) == [0, 1, 2, 3]

def test_2():
    assert dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 3) == [0, 1, 2, 3]

def test_3():
    assert dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3) == [3]

def test_4():
    assert dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 3) == [2, 3]

def test_5():
    assert dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0) == [0, 1]