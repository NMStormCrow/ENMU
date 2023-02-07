//  Assignment #2 -- C++
//  Thomas Crow
//  Using Python, C++, and Java create three programs to multiply
//  two square matrices of random integers between 1 and 10.
//  The sizes of these matrices are: 250, 500, 1000, 1500 and 2000
//  elements.
// 
//  In other words, multiply two 250x250 matrices, two 500x500
//  matrices, etc.


#include <cstdlib>
#include <iostream>

using namespace std;

class Matrix_Multiplication {

    public:

    void multiply_matrix(int matrix_size) {
        
        //Initialize 2D Arrays
        int matrixA[matrix_size][matrix_size];
        int matrixB[matrix_size][matrix_size];
        int matrixC[matrix_size][matrix_size];

        //Assign values to arrays
        for (int i=0; i<matrix_size; i++) {
            for (int j=0; j<matrix_size; j++) {
                matrixA[i][j] = (rand () % 10) + 1;
                matrixB[i][j] = (rand () % 10) + 1;
                matrixC[i][j] = 0;
            }           
        }

        //Assign matrixA * matrixB to matrixC
        for (int i=0; i<matrix_size; i++){
            for (int j=0; j<matrix_size; j++) {
                for (int k=0; k<matrix_size; k++) {
                    matrixC[i][j]+=matrixA[i][k]*matrixB[k][j];      
                }
            } 
        } 
    }
};

int main() {
    
    Matrix_Multiplication myMatrix;
    int matrix_size = 1500;
    myMatrix.multiply_matrix(matrix_size);

    return 0;
}
