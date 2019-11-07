from matplotlib import pyplot as plt
import math

# probability distribution function
# mu - mean
# sigma = standard deviation
def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return math.exp( -((x - mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))


xs = [x/10.0 for x in range(-50, 50)]
# standard normal distribution
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')

plt.plot(xs, [normal_pdf(x, sigma=1.5) for x in xs], '--', label='mu=0,sigma=1.5')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, mu=-2) for x in xs], '-.', label='mu=-2,sigma=1')
plt.legend()
plt.show()

