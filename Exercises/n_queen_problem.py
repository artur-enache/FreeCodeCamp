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

The first option that comes to mind is to create N random matrices of NxN size, where each matrix has a single Q
on each row, such that each column contains a single Q.

Afterwards, I need to check if any Q is placed diagonally from another. But I can't think about how DFS fits into this
approach. Perhaps the idea is to search "deep" on each diagonal. Example:

. Q . .
. . . Q
Q . . .
. . Q .

Start from the first Q. The diagonals are (clockwise): NE, SE, SW, NW

Or:
-1, 1
1, 1
1, -1
-1, -1

In the example above, the first valid diagonal to search for Q on row 0 is (1, 1); then the search starts at (0, 1) and
goes to element (0 + 1, 1 + 1), (1 + 1, 2 + 1) and stops.

And the second valid diagonal for the same Q is (1, -1); then the search starts at (0, 1) and goes to element
(0 + 1, 1 - 1) then stops.

If the DFS algorithm encounters a Q, it terminates early. If each diagonal DFS search is allowed to finish & exit, it
means there's no Q on said diagonal. If DFS searches all 4 diagonals successfully, it means the configuration of Q
is valid.

Then, move on to the next Q in the list & repeat the search.

Perhaps I don't even need to generate the initial N matrices to iterate over. I could:

add a queen at 0, 0
push the queen to the stack
for queen_index in range(1, N)
  pop the stack
  run DFS on all 8 directions
  if DFS does not find a Q:
    mark all the cells searched as "visited"
    save the Q's coordinates in the output_list[i] = j
    add a queen on the next row, and the first column not in visited
    if not possible:
      break
    push the Q
  else
    clear visited & output_list
    add a queen at 0, queen_index
    push the queen to the stack
"""
import pytest

def reset_board(queens: int) -> list[list[int]]:
    new_board = []
    for _ in range(queens):
        new_board.append([0 for _ in range(queens)])

    return new_board

def dfs_n_queens(queens: int) -> list[list[int]]:
    if queens < 1:
        return []

    board = reset_board(queens)

    stack = []
    board[0][0] = 1
    
    for q_index in range(1, queens):


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