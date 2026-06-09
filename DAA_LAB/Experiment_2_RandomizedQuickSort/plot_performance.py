import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]

times = [
    0.0001,
    0.0005,
    0.0012,
    0.0078,
    0.0185
]

plt.plot(sizes, times, marker='o')

plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Randomized Quick Sort Performance Analysis")

plt.grid(True)

# Save the plot for the manual/document
plt.savefig("RandomizedQuickSort_Performance.png")
plt.show()
