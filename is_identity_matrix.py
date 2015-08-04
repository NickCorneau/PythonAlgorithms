# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input, 
# define a  procedure that returns True if the input is an identity matrix 
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements 
# on the principal/main diagonal are 1 and all the elements outside 
# the principal diagonal are 0. 
# (A square matrix is a matrix in which the number of rows 
# is equal to the number of columns)

def is_identity_matrix(matrix):
    if (len(matrix) != len(matrix[0])):
        return False
    
    for i in range(len(matrix)):
        if (matrix[i][i] != 1):
            return False
        
    for row in matrix:
        one_counter = 0    
        
        for num in row:
            if (num != 0):
                one_counter = one_counter + 1
                if (one_counter > 1):
                    return False
    return True