import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]

times = [
    0.0001,
    0.0004,
    0.0010,
    0.0055,
    0.0125
]

plt.plot(sizes, times, marker='o')

plt.xlabel("Number of Passengers (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Binary Heap Priority Queue Performance")

plt.grid(True)

# Save the plot for the manual/document
plt.savefig("PriorityQueue_Performance.png")
plt.show()
