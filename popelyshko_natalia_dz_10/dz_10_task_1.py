import copy


class Matrix:
    matrix = [[]]

    def __init__(self, matrix_input: [[]]):
        self.matrix = matrix_input

    def __str__(self):
        result = ""
        for i in self.matrix:
            result += '| '+'\t'.join(map(str, i)) + ' |\n'
        return result

    def __add__(self, add_matrix):
        if len(self.matrix) != len(add_matrix.matrix):
            return None
        result = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                result[i][k] = self.matrix[i][k] + add_matrix.matrix[i][k]
        return Matrix(result)


lst = [[1, 2], [3, 4]]
matrix = Matrix(lst)
print(matrix)
lst2 = [[2, 4], [6, 8]]
matrix2 = Matrix(lst2)
print(matrix2)

matrix3 = matrix+matrix2
print(matrix3)