def antisymmetric(A):
    #Write your code here
    for row in range(len(A)):
        for col in range(len(A)):
            if (A[row][col] !=  A[col][row] * -1):
                return False
    return True
