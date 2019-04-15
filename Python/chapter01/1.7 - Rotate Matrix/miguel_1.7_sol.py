"""
Python version 3.7.0
1.7 - Rotate Matrix
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate
the image by 90 degrees.  Can you do this in place?
"""
import unittest
from typing import List, Callable


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


def rotate_matrix_in_place(matrix: List[List[int]], N: int) -> List[List[int]]:
    """
    Does the same as rotate_matrix, but in place.
    :param matrix: an NxN matrix
    :param N: the size of the matrix (NxN)
    :return:
    """
    return matrix


class TestRotateMatrixFunction(unittest.TestCase):
    def _run_tests(self, f: Callable[[List[List[int]], int], List[List[int]]]):
        cases = [
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
            )
        ]
        for matrix, N, expected in cases:
            self.assertEqual(f(matrix, N), expected, msg=(matrix, N, expected))

    def test_rotate_matrix(self):
        self._run_tests(rotate_matrix)
        # self._run_tests(rotate_matrix_in_place)


if __name__ == '__main__':
    unittest.main()
