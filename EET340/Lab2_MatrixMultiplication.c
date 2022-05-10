// Thomas Crow
// Lab #2 
// EET340

#include <stdio.h>

int main()
{

    int matrixA1[3] = {1,2,3};
    int matrixA2[3] = {4,5,6};
    int matrixB[3] = {4,4,4};

    int sum1 = 0;
    int sum2 = 0;

    for (int i = 0; i < 3; i++) {
        sum1 = sum1 + (matrixA1[i] * matrixB[i]);
    }

    for (int i = 0; i < 3; i++) {
        sum2 = sum2 + (matrixA2[i] * matrixB[i]);
    }

    printf("The result of the matrix multiplication is:\n");
    printf("%d\n", sum1);
    printf("%d\n", sum2);
    return 0;
}
     
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        

