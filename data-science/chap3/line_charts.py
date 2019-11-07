from matplotlib import pyplot as plt

variance     = [2**x for x in range(10)]
bias_squared = [2**x for x in range(9, -1, -1)]
total_error  = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance,  'g-', label='variance')
plt.plot(xs, bias_squared, 'r-.', label='bias^2')
plt.plot(xs, total_error, 'b:', label='total error')
plt.show()

