import math
from functools import reduce


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
