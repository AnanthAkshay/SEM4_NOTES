import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]

times = [
    0.0001,
    0.0007,
    0.0015,
    0.0102,
    0.0254
]

plt.plot(sizes, times, marker='o')

plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Merge Sort Performance Analysis")

plt.grid(True)

# Save the plot for the manual/document
plt.savefig("MergeSort_Performance.png")
plt.show()
