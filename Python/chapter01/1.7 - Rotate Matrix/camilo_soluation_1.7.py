"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel
in the image is 4 bytes, write a method to rotate the image by 90 degrees.
Can you do this in place?
Hints:#51, #100

"""


def rotate_matrix(matrix):
    matrix.reverse()# we frist reverse the matrix then we take its transpose

    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(i+1,n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp


matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate_matrix(matrix)
#[[7, 4, 1], [8, 5, 2], [9, 6, 3]]


print(matrix)
