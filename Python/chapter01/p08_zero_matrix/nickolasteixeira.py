#!/usr/bin/python3
import random
import unittest


def build_matrix(w, h, max=10):
    '''function that builds a matrix with random numbers including 0'''
    return [[random.randint(0, max) for _ in range(w)] for _ in range(h)]


def zero_matrix(matrix):
    '''Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.'''
    row, column = [], []
    zero_present = False

    for idx1 in range(len(matrix)):
        for idx2 in range(len(matrix[idx1])):
            if matrix[idx1][idx2] == 0:
                zero_present = True
                row.append(idx1)
                column.append(idx2)

    if zero_present:
        for idx1 in range(len(matrix)):
            for idx2 in range(len(matrix[idx1])):
                if idx1 in row:
                    matrix[idx1][idx2] = 0
                if idx2 in column:
                    matrix[idx1][idx2] = 0

class Test(unittest.TestCase):
    def test_rotate_matrix(self):
        matrix = [[9, 5, 7, 7],
                  [10, 4, 0, 10],
                  [1, 7, 3, 7],
                  [6, 8, 4, 4]]
        zero_matrix(matrix)
        self.assertEqual(
                matrix,
                [[9, 5, 0, 7],
                 [0, 0, 0, 0],
                 [1, 7, 0, 7],
                 [6, 8, 0, 4]])


if __name__ =='__main__':
    unittest.main()
