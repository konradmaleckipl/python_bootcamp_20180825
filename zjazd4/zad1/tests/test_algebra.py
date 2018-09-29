from zjazd4.zad1.mathematica.algebra import matrices as mat








def test_add_matrix():
    A = [[1,1,1],
         [2,2,2],
         [3,3,3]]
    B = [[3,3,3],
         [2,2,2],
         [1,1,1]]

    result_mat = mat.add_matrices(A, B)
    assert result_mat == [[4,4,4],
                          [4,4,4],
                          [4,4,4]]

def test_sub_matrix():
    A = [[1,1,1],
         [2,2,2],
         [3,3,3]]
    B = [[3,3,3],
         [2,2,2],
         [1,1,1]]

    result_mat = mat.sub_matrices(A, B)
    assert result_mat == [[-2,-2,-2],
                          [0,0,0],
                          [2,2,2]]