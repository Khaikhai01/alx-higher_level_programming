#!/usr/bin/python3
#if __name__ == '__main__':
def square_matrix_simple(matrix=[]):
    return (list(map(lambda x :list(map(lambda y: (y**2), x)),matrix )))
