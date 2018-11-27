"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel
in the image is 4 bytes, write a method to rotate the image by 90 degrees.
Can you do this in place?
Hints:#51, #100

"""


def rotate_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(i+1,n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    #flip_it(matrix)
#This give us the transpose of a matrix. Now we need to flip it on its image
"""
def flip_it(matrix):
    row = len(matrix)-1
    col = len(matrix[0])-1

    for i in range(row):
        for j in range(col/2):
            matrix[i][j],matrix[ i][col - 1 - j] = matrix[ i][col - 1 - j] ,matrix[i][j]

"""


matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate_matrix(matrix)
#flip_it(matrix)
print(matrix)
