#!/usr/bin/python3
import random
from pprint import pprint

def build_matrix(w, h, max=10):
    '''function that builds a matrix with random numbers including 0'''
    return [[random.randint(0, max) for _ in range(w)] for _ in range(h)]

def rotate_matrix(matrix):
    '''function that rotates a matrix clockwise'''
    if (len(matrix) is 0 or len(matrix) is not len(matrix[0])): return False
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

if __name__ =='__main__':
    matrix = build_matrix(5, 5)
    pprint(matrix)
    rotate_matrix(matrix)
    pprint(matrix)
