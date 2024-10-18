matrix1 = [[2, 1, 4], [1, -2, 2], [-1, 1, 0]]
matrix2 = [[0.2, -0.4, -1], [0.2, -0.4, 0], [0.1, 0.3, 0.5]]

def matrix_multiply(matrix1, matrix2):
    # Get dimensions of the matrices
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    # Check if matrices can be multiplied
    if cols_matrix1 != rows_matrix2:
        return None  # Matrices cannot be multiplied

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    # Multiply the matrices
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def is_identity_matrix(matrix):
    # Check if matrix is square
    if len(matrix) != len(matrix[0]):
        return False

    # Check if it is close to an identity matrix by rounding
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j and round(matrix[i][j], 8) != 1:
                return False
            elif i != j and round(matrix[i][j], 8) != 0:
                return False
    
    return True

def check_matrices_inverse(matrix1, matrix2):
    # Multiply matrix1 and matrix2
    product = matrix_multiply(matrix1, matrix2)
    
    if product is None:
        return "Matrices cannot be multiplied, so they are not inverses."

    # Check if the product is the identity matrix
    if is_identity_matrix(product):
        return "The matrices are inverses of each other."
    else:
        return "The matrices are not inverses of each other."


result = check_matrices_inverse(matrix1, matrix2)
print(result)
