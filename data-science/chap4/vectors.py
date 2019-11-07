import math
import random
from collections import Counter
from functools import reduce

def vector_add(v, w):
    """adds corresponding elements"""
    return [vi + wi for vi, wi in zip(v, w)]

def vector_substract(v, w):
    return [vi - wi for vi, wi in zip(v, w)]

# def vector_sum(vectors):
#     """sums all corresponding elements"""
#     result = vectors[0]
#     for vector in vectors[1:]:
#         result = vector_add(result, vector)
#     return result

def vector_sum(vectors):
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    return [c * vi for vi in v]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

# project v -> w
def dot(v, w):
    return sum(vi * wi for vi, wi in zip(v, w))

def sum_of_squares(v):
    return dot(v, v)

def magnitude(v):
    math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    return sum_of_squares(vector_substract(v, w))

def distance(v, w):
    return magnitude(vector_substract(v, w))

assert(vector_add([1,2], [2,1]) == [3,3])
assert(vector_substract([2,1], [2,1]) == [0,0])
assert(vector_sum([[1,2], [3,4], [5,6]]) == [9,12])
assert(scalar_multiply(2, [1,2]) == [2,4])
assert(vector_mean([[1,2], [3,4], [5,6]]) == [3,4])
assert(dot([1,2], [3,4]) == 11)


friends = [random.randint(10,50) for _ in range(10)]
daily_minutes = [random.randint(1,60) for _ in range(10)]

print(friends)
print('sorted: ', sorted(friends))
print('max: ', max(friends))
print('min: ', min(friends))

# halfway point between the points
def mean(v):
    return sum(v) / len(v)

def median(v):
    sorted_v = sorted(v)
    n = len(v)
    midpoint = n // 2

    # If v is odd-length, use midpoint.
    # If even, get the average of the 2 middle points
    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return ((sorted_v[lo] + sorted_v[hi]) / 2)


print('mean: ', mean(friends))
print('median: ', median(friends))

# p-percent of the data is less than this value
def quantile(v, p):
    i = int(len(v) * p)
    return sorted(v)[i]

print('quantile 10%: ', quantile(friends, 0.10))
print('quantile 50%: ', quantile(friends, 0.50))


print(Counter(friends))


# dispersion : how spread the data is

def data_range(v):
    return max(v) - min(v)

print(data_range(friends))


# deviations from the mean
def de_mean(v):
    vbar = mean(v)
    return [vi - vbar for vi in v]


# variance
def variance(v):
    n = len(v)
    deviations = de_mean(v)
    return sum_of_squares(deviations) / (n - 1)

print(de_mean(friends))
print(variance(friends))

def standard_deviation(v):
    return math.sqrt(variance(v))

print(standard_deviation(friends))

def interquartile_range(v):
    return quantile(v, 0.75) - quantile(v, 0.25)

print(interquartile_range(friends))


def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) /  (n - 1)


print(covariance(friends, daily_minutes))

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)

    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0

print(correlation(friends, daily_minutes))
