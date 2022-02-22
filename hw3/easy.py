import numpy as np

class My_Matrix:
    def __init__(self, data):
        self.data = data
        self.n_rows = len(self.data)
        self.n_columns = len(self.data[0])

    def __add__(self, other):
        return

    def __mul__(self, other):
        return

    def __matmul__(self, other):
        return

if __name__ == '__main__':
    path = 'artifacts/easy'
