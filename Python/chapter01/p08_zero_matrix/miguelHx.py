"""
Python version 3.7.0
1.8 - Zero Matrix
Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0
"""
import unittest
from typing import List


def zero_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    zero_matrix will take in an MxN matrix and when a 0 element is found,
    the whole column and row will be set to 0.
    The algorithm works by first scanning for
    rows and columns where there is a 0 and store into a set.
    Then we go through each stored row and column indices
    and proceed to set the rows and columns to 0.
    Runtime: O(M * N)
    Space Complexity: O(M + N)
    :param matrix: an MxN matrix.  M is the number of rows, N is the number of columns
    :return: a zero-modified matrix
    """
    M = len(matrix)
    N = len(matrix[0])

    rows_to_zero = set()
    cols_to_zero = set()
    # first, scan for coordinates of 0s
    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if num != 0:
                continue
            # otherwise, save row or col to rows or cols to zero set
            rows_to_zero.add(i)
            cols_to_zero.add(j)
    for i in rows_to_zero:
        # set row to 0 by looping through columns of current row
        for k in range(N):
            matrix[i][k] = 0

    for j in cols_to_zero:
        # set column to 0 by looping through rows of current column
        for l in range(M):
            matrix[l][j] = 0
    return matrix


class TestZeroMatrixFunction(unittest.TestCase):

    def setUp(self):
        self.cases = [
            (
                [
                    [1, 2, 3, 4],
                    [5, 6, 0, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]
                ],
                [
                    [1, 2, 0, 4],
                    [0, 0, 0, 0],
                    [9, 10, 0, 12],
                    [13, 14, 0, 16]
                ]
            ),
            (
                [
                    [1, 2],
                    [3, 4],
                    [5, 6],
                    [7, 8],
                    [9, 0]
                ],
                [
                    [1, 0],
                    [3, 0],
                    [5, 0],
                    [7, 0],
                    [0, 0]
                ],
            ),
            (
                [
                    [1, 2],
                    [0, 4],
                    [5, 6],
                    [7, 8],
                    [9, 0]
                ],
                [
                    [0, 0],
                    [0, 0],
                    [0, 0],
                    [0, 0],
                    [0, 0]
                ]
            ),
            (
                [
                    [1, 2, 3, 4, 5, 6, 0, 8, 9],
                    [9, 8, 7, 6, 5, 4, 3, 2, 1],
                ],
                [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [9, 8, 7, 6, 5, 4, 0, 2, 1],
                ]
            ),
            (
                [
                    [0]
                ],
                [
                    [0]
                ]
            ),
            (
                [
                    [1]
                ],
                [
                    [1]
                ]
            ),
            (
                [
                    [1, 2],
                    [3, 4]
                ],
                [
                    [1, 2],
                    [3, 4]
                ]
            ),
            (
                [
                    [0, 1, 2],
                    [0, 3, 4],
                    [0, 5, 6],
                    [0, 7, 8]
                ],
                [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]
            ),
            (
                [
                    [1, 2, 3, 4],
                    [5, 6, 0, 8],
                    [9, 10, 0, 12],
                    [13, 14, 15, 16]
                ],
                [
                    [1, 2, 0, 4],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [13, 14, 0, 16]
                ]
            ),
            (
                [
                    [0, 0, 0, 0],
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]
                ],
                [
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]
                ]
            ),
            (
                [[0] * 1000 for _ in range(1000)],
                [[0] * 1000 for _ in range(1000)],
            )
        ]

    def test_zero_matrix(self):
        for matrix, expected in self.cases:
            self.assertEqual(zero_matrix(matrix), expected, msg=(matrix, expected))


if __name__ == '__main__':
    unittest.main()
