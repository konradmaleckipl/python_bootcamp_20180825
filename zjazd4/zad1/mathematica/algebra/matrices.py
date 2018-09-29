

def add_matrices(mat_a, mat_b):
    result = [[mat_a[i][j] + mat_b[i][j] for j in range(len(mat_a[0]))] for i in range(len(mat_a))]
    return result

def sub_matrices(mat_a, mat_b):
    result = [[mat_a[i][j] - mat_b[i][j] for j in range(len(mat_a[0]))] for i in range(len(mat_a))]
    return result