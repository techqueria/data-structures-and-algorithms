#!/usr/bin/python3
import random


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
            if matrix[idx1][idx2] is 0:
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

if __name__ == '__main__':
    matrix = build_matrix(4, 4)
    print("Old Matrix => ", matrix)
    zero_matrix(matrix)
    print("New Matrix => ", matrix)
