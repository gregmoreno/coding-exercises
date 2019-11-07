from matplotlib import pyplot as plt
import random

friends = [random.randint(1, 100) for i in range(10)]
minutes = [random.randint(101, 200) for i in range(10)]
labels  = [c for c in 'abcdefghi']

plt.scatter(friends, minutes)
plt.axis('equal')  # set scale equal variation


# label each point
for label, fiend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(fiend_count, minute_count),  # put label with its point
                 xytext=(5, -5),                  # slightly offset
                 textcoords='offset points')
plt.show()
