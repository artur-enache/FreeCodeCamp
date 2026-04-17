"""Adjacency List to Matrix Converter"""

import pytest

def adjacency_list_to_matrix(adj_list: dict) -> list:
    matrix = []
    for _ in range(len(adj_list)):
        matrix.append([0] * len(adj_list))

    for key in adj_list.keys():
        for elem in adj_list[key]:
            matrix[key][elem] = 1

    print('\n'.join(str(n) for n in matrix))
    return matrix

def test_1():
    assert (adjacency_list_to_matrix({0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}) ==
            [[0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]])

def test_2():
    assert adjacency_list_to_matrix({0: [1], 1: [0]}) == [[0, 1], [1, 0]]

def test_3():
    assert adjacency_list_to_matrix({0: [], 1: [], 2: []}) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]