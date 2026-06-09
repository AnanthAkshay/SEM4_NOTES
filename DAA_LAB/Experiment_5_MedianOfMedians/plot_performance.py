import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]

times = [
    0.0001,
    0.0002,
    0.0005,
    0.0025,
    0.0051
]

plt.plot(sizes, times, marker='o')

plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Median Selection Performance Analysis")

plt.grid(True)

# Save the plot for the manual/document
plt.savefig("MedianOfMedians_Performance.png")
plt.show()
