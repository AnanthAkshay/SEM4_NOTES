import matplotlib.pyplot as plt

sizes = [10, 20, 30, 40, 50]

times = [
    0.0001,
    0.0005,
    0.0015,
    0.0035,
    0.0065
]

plt.plot(sizes, times, marker='o')

plt.xlabel("Number of Matrices")
plt.ylabel("Execution Time (seconds)")
plt.title("Matrix Chain Multiplication Performance")

plt.grid(True)

# Save the plot for the manual/document
plt.savefig("MCM_Performance.png")
plt.show()
