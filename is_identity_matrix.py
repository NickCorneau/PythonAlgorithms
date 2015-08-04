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
