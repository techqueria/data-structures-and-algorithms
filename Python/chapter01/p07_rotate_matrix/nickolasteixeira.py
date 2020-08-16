#!/usr/bin/python3

import random
import unittest


def build_matrix(w, h, max=10):
    '''function that builds a matrix with random numbers including 0'''
    return [[random.randint(0, max) for _ in range(w)] for _ in range(h)]

def rotate_matrix(matrix):
    '''function that rotates a matrix clockwise'''
    if (len(matrix) == 0 or len(matrix) is not len(matrix[0])): return False
    matrix_length = len(matrix)
    for layer in range(matrix_length//2):
        first = layer
        last = matrix_length - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]

            ######################
            #  a  ---------->  d #
            #  ^               | #
            #  |               | #
            #  |               | #
            #  |               v #
            #  b <------------ c #
            #######################

            # top left inherits from bottom bottom left
            matrix[first][i] = matrix[last - offset][first]

            # bottom left becomes bottom right
            matrix[last - offset][first] = matrix[last][last - offset]

            # bottom right becomes top right
            matrix[last][last - offset] = matrix[i][last]

            # top right becomes top left
            matrix[i][last] = top


class Test(unittest.TestCase):
    def test_rotate_matrix(self):
        matrix = [[8, 0, 5, 6, 8],
                  [3, 4, 6, 6, 8],
                  [3, 2, 10, 3, 0],
                  [4, 3, 9, 0, 2],
                  [9, 5, 4, 2, 10]]
        rotate_matrix(matrix)
        self.assertEqual(
                matrix,
                [[9, 4, 3, 3, 8],
                 [5, 3, 2, 4, 0],
                 [4, 9, 10, 6, 5],
                 [2, 0, 3, 6, 6],
                 [10, 2, 0, 8, 8]])


if __name__ =='__main__':
    unittest.main()
