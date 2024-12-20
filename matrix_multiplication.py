#each sublist -> row in matrix
matrix1 = [[1,2,3],[1,4,5]]
matrix2 = [[2,3],[5,3],[1,5]]

#function returns: matrix1 * matrix2
def matrix_multiplication(matrix1, matrix2):
    if (len(matrix1) != len(matrix2[0])):
        return False

    res_matrix = []
    for rows1 in range(len(matrix1)):
        res_matrix.append([])
        for columns2 in range(len(matrix2[0])):
            res_matrix[rows1].append(0)
            for rows2 in range(len(matrix2)):
                res_matrix[rows1][columns2] += matrix1[rows1][rows2]*matrix2[rows2][columns2]

    return res_matrix


MATRIX = matrix_multiplication(matrix1, matrix2)
print(MATRIX)