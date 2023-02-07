#  Assignment #2 -- Python
#  Thomas Crow
#
#  Using Python, C++, and Java create three programs to multiply
#  two square matrices of random integers between 1 and 10.
#  The sizes of these matrices are: 250, 500, 1000, 1500 and 2000
#  elements.
#  
#  In other words, multiply two 250x250 matrices, two 500x500
#  matrices, etc.

import random


def multiply_matrix(matrix_size):

    #Initialize 2D Arrays
    matrixA=[]
    matrixB=[]
    matrixC=[]
    for i in range(matrix_size):
        matrixA_column_elements=[]
        matrixB_column_elements=[]
        matrixC_column_elements=[]
        #Assign values to arrays
        for j in range(matrix_size):
            matrixA_column_elements.append(random.randint(1, 10))
            matrixB_column_elements.append(random.randint(1, 10))
            matrixC_column_elements.append(0)
        matrixA.append(matrixA_column_elements)
        matrixB.append(matrixB_column_elements)
        matrixC.append(matrixC_column_elements)
    #Assign matrixA * matrixB to matrixC
    for i in range(matrix_size):
        for j in range(matrix_size):
            for k in range(matrix_size): 
                matrixC[i][j] = matrixA[i][k] * matrixB[k][j]


def main():

    matrix_size = 1500
    multiply_matrix(matrix_size)

main()