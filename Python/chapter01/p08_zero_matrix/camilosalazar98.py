"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.
Hints:#17, #74, #702



I've been stuck on this for a couple of days..
Really good resource:
https://www.youtube.com/watch?v=ZzpJgRvqSJQ&t=113s
https://www.youtube.com/watch?v=qWeNXOCff3o&t=408s
"""

import unittest


def zeroMatrix(matrix):
    rowZero = False
    colZero = False

    for i in range(0,len(matrix)):
        if matrix[i][0] == 0:
            colZero = True

    for i in range(0,len(matrix[0])):
        if matrix[0][i] == 0:
            rowZero = True

    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[0][j] == 0
                matrix[i][0] == 0


    for i in range(1,len(matrix)):
        if(matrix[i][0] == 0):
            for j in range(1,len(matrix[0])):
                matrix[i][j] = 0

    for i in range(1,len(matrix[0])):
        if(matrix[0][i] == 0):
            for j in range(1,len(matrix)):
                matrix[i][j] = 0

    if rowZero:
        for i in range(0,len(matrix[0])):
            matrix[0][i] = 0

    if colZero:
        for i in range(0,len(matrix)):
            matrix[i][0] = 0


class Test(unittest.TestCase):
    def test_rotate_matrix(self):
        matrix = [[0,1,1],
                  [1,1,1],
                  [1,1,1]]
        zeroMatrix(matrix)
        self.assertEqual(matrix,
                         [[0,0,0],
                          [0,1,1],
                          [0,1,1]])


if __name__ =='__main__':
    unittest.main()
