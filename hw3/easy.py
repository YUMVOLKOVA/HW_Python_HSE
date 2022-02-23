import numpy as np

def check_implementation(list_1, list_2, matrix_1, matrix_2, action):
    if action == 'add':
        print('add')
        return (matrix_1 + matrix_2) == (np.array(list_1) + np.array(list_2))
    if action == 'mul':
        print('mul')
        return (matrix_1 * matrix_2) == (np.array(list_1) * np.array(list_2))
    if action == 'matmul':
        print('matmul')
        return (matrix_1 @ matrix_2) == (np.array(list_1) @ np.array(list_2))

def save_results(data, path):
    with open(path, "w") as f:
        f.write(data)
        f.close()

class My_Matrix:
    def __init__(self, data):
        self.data = data
        self.n_rows = len(self.data)
        self.n_columns = len(self.data[0])

    def __add__(self, other):
        if self.n_rows != other.n_rows or self.n_columns != other.n_columns:
            raise Exception('check the size of the matrices')
        else:
            sum_of_matrix = []
            for row in zip(self.data, other.data):
                sum_of_matrix.append(list(map(sum, zip(*row))))
        return My_Matrix(sum_of_matrix)

    def __mul__(self, other):
        if self.n_rows != other.n_rows or self.n_columns != other.n_columns:
            raise Exception('check the size of the matrices')
        else:
            mul_of_matrix = []
            for row in zip(self.data, other.data):
                row_mul = []
                for i, j in zip(*row):
                    row_mul.append(i * j)
                mul_of_matrix.append(row_mul)
        return My_Matrix(mul_of_matrix)

    def __matmul__(self, other):
        if self.n_columns != other.n_rows:
            raise Exception('check the size of the matrices')
        matmul_of_matrix = []
        for data_row in self.data:
            row_mul = []
            for other_row in zip(*other.data):
                row_mul.append(sum(i * j for i, j in zip(data_row, other_row)))
            matmul_of_matrix.append(row_mul)
        return My_Matrix(matmul_of_matrix)

    def __str__(self):
        a = '['
        for i, row in enumerate(X):
            if i != len(X) - 1:
                a += ''.join(str(row)) + '\n'
            else:
                a += ''.join(str(row)) + ']'
        return a

if __name__ == '__main__':
    np.random.seed(0)
    list_1 = np.random.randint(0, 10, (10, 10))
    list_2 = np.random.randint(0, 10, (10, 10))

    matrix_1 = My_Matrix(data=list_1)
    matrix_2 = My_Matrix(data=list_2)

    path = 'artifacts/easy'
    print(check_implementation(list_1, list_2, matrix_1, matrix_2, 'add'))
    save((matrix_1 + matrix_2).__str__(), f'{path}/matrix+.txt')
    print(check_implementation(list_1, list_2, matrix_1, matrix_2, 'mul'))
    save((matrix_1 * matrix_2).__str__(), f'{path}/matrix*.txt')
    print(check_implementation(list_1, list_2, matrix_1, matrix_2, 'matmul'))
    save((matrix_1 @ matrix_2).__str__(), f'{path}/matrix@.txt')


