import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]

times = [
    0.0001,
    0.0002,
    0.0003,
    0.0015,
    0.0030
]

plt.plot(sizes, times, marker='o')

plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Counting Sort Performance Analysis")

plt.grid(True)

# Save the plot for the manual/document
plt.savefig("CountingSort_Performance.png")
plt.show()
