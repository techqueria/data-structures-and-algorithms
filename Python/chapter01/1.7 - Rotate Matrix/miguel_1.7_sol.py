"""
Python version 3.7.0
1.7 - Rotate Matrix
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate
the image by 90 degrees.  Can you do this in place?
"""
import unittest
from typing import List


def rotate_matrix(matrix: List[List[int]], N: int) -> List[List[int]]:
    """
    Rotate matrix will rotate the given matrix by 90 degrees.
    Runtime: O(N^2), asymptotic runtime depends on N
    Space Complexity: O(N^2), creating a new matrix of NxN called 'rotated'
    :param matrix: an NxN matrix
    :param N: the size of the matrix (NxN)
    :return: a newly rotated matrix
    """
    rotated = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            rotated[j][(N-1)-i] = matrix[i][j]
    return rotated


def rotate_matrix_in_place(matrix: List[List[int]], start_row: int, start_col: int, N: int) -> List[List[int]]:
    """
    Does the same as rotate_matrix, but in place.
    Runtime: O(N^2), asymptotic runtime depends on N. We make N^2 swaps.
    Space Complexity: O(1), constant amount of temp variables that does not depend on N.
                        Note: I am assuming that compiler will optimize the tail recursion.
    :param matrix: an NxN matrix
    :param start_row: starting row index
    :param start_col: starting col index
    :param N: the size of the matrix (NxN)
    :return: the input matrix, but rotated
    """
    num_rotations = 4
    if N == 0 or N == 1:
        return matrix
    col = start_col
    while True:
        rotated_row = start_row
        rotated_col = col
        temp_new = matrix[start_row][col]
        for r in range(0, num_rotations):
            temp = temp_new
            # compute new rotated indices
            prev_col = rotated_col
            rotated_col = N - 1 - rotated_row + (start_row * 2)  # offset to account for reduced N
            rotated_row = prev_col
            # store value at newly computed indices
            temp_new = matrix[rotated_row][rotated_col]
            matrix[rotated_row][rotated_col] = temp
        if col - start_col >= N - 2:
            break
        col = col + 1
    return rotate_matrix_in_place(matrix, start_row + 1, start_col + 1, N - 2)


class TestRotateMatrixFunction(unittest.TestCase):

    def setUp(self):
        self.cases = [
            (
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]
                ],
                4,
                [
                    [13, 9, 5, 1],
                    [14, 10, 6, 2],
                    [15, 11, 7, 3],
                    [16, 12, 8, 4]
                ]
            ),
            (
                [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ],
                3,
                [
                    [7, 4, 1],
                    [8, 5, 2],
                    [9, 6, 3]
                ]
            ),
            (
                [
                    [1]
                ],
                1,
                [
                    [1]
                ]
            ),
            (
                [
                    [1, 2, 3, 4, 5, 6],
                    [7, 8, 9, 10, 11, 12],
                    [13, 14, 15, 16, 17, 18],
                    [19, 20, 21, 22, 23, 24],
                    [25, 26, 27, 28, 29, 30],
                    [31, 32, 33, 34, 35, 36]
                ],
                6,
                [
                    [31, 25, 19, 13, 7, 1],
                    [32, 26, 20, 14, 8, 2],
                    [33, 27, 21, 15, 9, 3],
                    [34, 28, 22, 16, 10, 4],
                    [35, 29, 23, 17, 11, 5],
                    [36, 30, 24, 18, 12, 6]
                ]
            ),
            (
                [
                    [1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20],
                    [21, 22, 23, 24, 25]
                ],
                5,
                [
                    [21, 16, 11, 6, 1],
                    [22, 17, 12, 7, 2],
                    [23, 18, 13, 8, 3],
                    [24, 19, 14, 9, 4],
                    [25, 20, 15, 10, 5]
                ]
            ),
            (
                [
                    [1, 2, 3, 4, 5, 6, 7],
                    [8, 9, 10, 11, 12, 13, 14],
                    [15, 16, 17, 18, 19, 20, 21],
                    [22, 23, 24, 25, 26, 27, 28],
                    [29, 30, 31, 32, 33, 34, 35],
                    [36, 37, 38, 39, 40, 41, 42],
                    [43, 44, 45, 46, 47, 48, 49]
                ],
                7,
                [
                    [43, 36, 29, 22, 15, 8, 1],
                    [44, 37, 30, 23, 16, 9, 2],
                    [45, 38, 31, 24, 17, 10, 3],
                    [46, 39, 32, 25, 18, 11, 4],
                    [47, 40, 33, 26, 19, 12, 5],
                    [48, 41, 34, 27, 20, 13, 6],
                    [49, 42, 35, 28, 21, 14, 7]
                ]
            )
        ]

    def test_rotate_matrix(self):
        for matrix, N, expected in self.cases:
            self.assertEqual(rotate_matrix(matrix, N), expected, msg=(matrix, N, expected))

    def test_rotate_matrix_in_place(self):
        start_row = 0
        start_col = 0
        for matrix, N, expected in self.cases:
            self.assertEqual(rotate_matrix_in_place(matrix, start_row, start_col, N), expected, msg=(matrix, N, expected))


if __name__ == '__main__':
    unittest.main()
