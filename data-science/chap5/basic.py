import random
from collections import Counter

friends = [random.randint(10,50) for _ in range(10)]

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

