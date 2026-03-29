"""
PROBLEM TEXT:
Given an integer n, return the nth row of Pascal's triangle as an array.

In Pascal's Triangle, each row begins and ends with 1, and each interior value is the sum of the two values directly above it.
"""

def pascal_row(n):
    if n == 1:
        primary = [1]
    else:
        primary = [1] + [0] * (n - 2) + [1]
    secondary = primary[:]
    for i in range(1, n):
        for index, element in enumerate(primary):
            if index == 0 or index == n-1:
                pass
            else:
                secondary[index] = element + primary[index-1]
        primary = secondary[:]

    return primary

print(pascal_row(4))

# As bonus practice, this algorithm has a quadratic time & space complexity O(n^2) because of the two nested 'for' loops

