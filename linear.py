import math
from functools import reduce


# Vectors

def vector_add(v1, v2):
    """Returns addition of 2 vectors (v1 + v2)"""
    return [
        v1_el + v2_el
        for v1_el, v2_el in zip(v1, v2)
    ]


def vector_subtract(v1, v2):
    """Return subtract of 2 vectors (v1 - v2)"""
    return [
        v1_el - v2_el
        for v1_el, v2_el in zip(v1, v2)
    ]


def vector_sum(vectors):
    """Return sum of given vectors"""
    return reduce(vector_add, vectors)


def scalar_multiply(factor, vector):
    """Returns vector multiplied by given factor"""
    return [vector_el * factor for vector_el in vector]


def vector_mean(vectors):
    """Returns vector that consists of average values of given vectors"""
    length = len(vectors)
    return scalar_multiply(1 / length, vector_sum(vectors))


def dot(v1, v2):
    """v1_1 * v2_1 + ... + v1_n * v2_n"""
    return sum(
        v1_i * v2_i
        for v1_i, v2_i in zip(v1, v2)
    )


def sum_of_squares(vector):
    """v_1 * v_1 + ... + v_n * v*n"""
    return dot(vector, vector)


def magnitude(vector):
    return math.sqrt(sum_of_squares(vector))


def squared_distance(v1, v2):
    """(v1_1 - v2_1) ** 2 + ... + (v1_n - v2_n) ** 2"""
    return sum_of_squares(vector_subtract(v1, v2))


def distance(v1, v2):
    return magnitude(vector_subtract(v1, v2))


# Matrices

def shape(A):
    return len(A), len(A[0])


def get_row(A, i):
    return A[i]


def get_column(A, j):
    return [
        row[j]
        for row in A
    ]


def make_matrix(num_rows, num_columns, entry_fn):
    """Returns matrix of size num_rows x num_columns,
    where element (i, j) equals value of function entry_fn(i, j)"""
    return [
        [
            entry_fn(i, j)
            for j in range(num_columns)
        ]
        for i in range(num_rows)
    ]


def is_diagonal(i, j):
    """1 in diagonal, others are 0"""
    return 1 if i == j else 0















