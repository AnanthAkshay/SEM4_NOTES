import matplotlib.pyplot as plt

sizes = [
    100,
    500,
    1000,
    5000,
    10000
]

times = [
    0.0001,
    0.0004,
    0.0009,
    0.0050,
    0.0110
]

plt.plot(
    sizes,
    times,
    marker='o'
)

plt.xlabel("Number of Nodes")

plt.ylabel(
    "Execution Time (seconds)"
)

plt.title(
    "DFS Performance Analysis"
)

plt.grid(True)

# Save the plot for the manual/document
plt.savefig("DFS_Performance.png")
plt.show()
