import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin
from numbers import Number

def check_implementation(list_1, list_2, matrix_1, matrix_2, action):
    if action == 'add':
        print('add')
        return np.array((matrix_1 + matrix_2).data) == (np.array(list_1) + np.array(list_2))
    if action == 'mul':
        print('mul')
        return np.array((matrix_1 * matrix_2).data) == (np.array(list_1) * np.array(list_2))
    if action == 'matmul':
        print('matmul')
        return np.array((matrix_1 @ matrix_2).data) == (np.array(list_1) @ np.array(list_2))

class BeautifulPrint:
    def __str__(self):
        a = '['
        for i, row in enumerate(self.data):
            if i != len(self.data) - 1:
                a += ','.join(row) + '\n'
            else:
                a += ''.join(str(row)) + ']'
        return a

class SaveFile:
    def save_result(self, path):
        f = open(path, "w")
        f.write(self.__str__())
        f.close()

class MValue:
    def __init__(self, value):
        self.data_value = np.asarray(value)

    @property
    def data(self):
        return self.data_value

    @data.setter
    def data(self, value):
        self.data_value = value

class My_Matrix_Medium(NDArrayOperatorsMixin, BeautifulPrint, MValue, SaveFile):
    '''
    https://numpy.org/doc/stable/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html
    '''
    _HANDLED_TYPES = (np.ndarray, Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get("out", ())

        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (My_Matrix_Medium,)):
                return NotImplemented

        inputs = tuple(x.data if isinstance(x, My_Matrix_Medium) else x for x in inputs)
        if out:
            kwargs["out"] = tuple(x.data if isinstance(x, My_Matrix_Medium) else x for x in out)

        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)

        elif method == "at":
            return None

        else:
            return type(self)(result)

if __name__ == '__main__':
    np.random.seed(0)
    list_1 = np.random.randint(0, 10, (10, 10))
    list_2 = np.random.randint(0, 10, (10, 10))

    matrix_1 = My_Matrix_Medium(value=list_1)
    matrix_2 = My_Matrix_Medium(value=list_2)

    path = 'artifacts/medium'
    print(f'matrix_1: \n {matrix_1.data}')
    print(f'matrix_2: \n {matrix_2.data}')
    print(f'matrix_1 str: \n {matrix_1.__str__()}')
    print(f'matrix_2 str: \n {matrix_2.__str__()}')
    print(check_implementation(list_1, list_2, matrix_1, matrix_2, 'add'))
    (matrix_1 + matrix_2).save_result(f'{path}/matrix+.txt')
    print(check_implementation(list_1, list_2, matrix_1, matrix_2, 'mul'))
    (matrix_1 * matrix_2).save_result(f'{path}/matrix*.txt')
    print(check_implementation(list_1, list_2, matrix_1, matrix_2, 'matmul'))
    (matrix_1 @ matrix_2).save_result(f'{path}/matrix@.txt')

