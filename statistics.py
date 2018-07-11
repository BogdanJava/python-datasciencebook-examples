import math
from collections import Counter

from linear import sum_of_squares


def mean(x):
    """Average value of dataset"""
    return sum(x) / len(x)


def median(v):
    """Returns the nearest value to the center of vector v"""
    length = len(v)
    sorted_v = sorted(v)
    midpoint = length // 2

    if length % 2 == 1:
        return sorted_v[midpoint]
    else:
        before_center = midpoint - 1
        after_center = midpoint
        return (sorted_v[before_center] + sorted_v[after_center]) / 2


def quantile(data, percentage):
    """
    Returns the value in 'data' that has
    'percentage' percent of data before itself
    """
    p_index = int(percentage * len(data))
    return sorted(data)[p_index]


def mode(data):
    """Returns an array of the most popular values"""
    counts = Counter(data)
    max_count = max(counts.values())
    return [
        value for value, count in counts.items()
        if count == max_count
    ]


def data_range(data):
    """Return the difference between the max and min element in 'data'"""
    return max(data) - min(data)


# vector of deviation from average value
def de_mean(data):
    """
    Recalculate dataset by substracting the average value of dataset from
    each element of the dataset
    """
    x_bar = mean(data)
    return [x_i - x_bar for x_i in data]


# dispersion
def variance(data):
    """
    Calculates the variance of dataset

    It's assumed that 'data' has at least 2 elements
    """
    length = len(data)
    deviations = de_mean(data)
    return sum_of_squares(deviations) / (length - 1)


def standard_deviation(data):
    return math.sqrt(variance(data))


def interquartile_range(data):
    return quantile(data, 0.75) - quantile(data, 0.25)

