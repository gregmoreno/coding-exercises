from matplotlib import pyplot as plt

movies = ["Annie Hall",  "Ben Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

plt.bar([i for i, _ in enumerate(num_oscars)], num_oscars)
plt.xticks([i for i, _ in enumerate(movies)], movies)
plt.show()
