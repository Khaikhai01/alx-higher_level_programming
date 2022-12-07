#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = lambda x: x**2
    squared = [list(map(square, sublist)) for sublist in matrix]
    return squared
