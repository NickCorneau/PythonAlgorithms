# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(A):
    #Write your code here
    for row in range(len(A)):
        for col in range(len(A)):
            if (A[row][col] !=  A[col][row] * -1):
                return False
    return True