from collections import Counter
from matplotlib import pyplot as plt
from statistics import *

num_friends = [
    100, 59, 23, 52, 25, 12, 12,
    89, 49, 21, 44, 12, 20, 51, 30, 12,
    100, 59, 23, 52, 12, 12,
    89, 44, 12, 20, 51, 30, 12,
    100, 59, 23, 55, 25, 12, 12,
    89, 49, 21, 44, 12, 20,
    89, 44, 12, 20, 51, 30, 12,
    100, 59, 12,
    89, 49, 21, 44, 12, 20, 44, 44, 44,
    44, 44, 44, 44, 44, 44, 44
]

num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)
sorted_values = sorted(num_friends)

r = range(0, 5)
print('sorted set:', list(r))
print('average value:', mean(r))
print('de_mean:', de_mean(r))
print('variance: ', variance(r))
print('standard deviation: ', standard_deviation(r))
print('interquartile range: ', interquartile_range(r))