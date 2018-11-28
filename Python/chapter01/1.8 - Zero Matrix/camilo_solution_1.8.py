"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.
Hints:#17, #74, #702
"""



def zeroMatrix(matrix):
    m = len(matrix) - 1
    n = len(matrix[0]) - 1
    for i in range(m):
        for j in range(n):
                if matrix[i][j]  == 0:
                    matrix[i+1][j] = 0


matrix = [[0,1,2],[3,4,5],[6,7,8]]


zeroMatrix(matrix)
print(matrix)
