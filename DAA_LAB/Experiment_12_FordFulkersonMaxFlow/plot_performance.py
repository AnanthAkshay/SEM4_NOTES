import matplotlib.pyplot as plt

sizes = [
    100,
    500,
    1000,
    5000,
    10000
]

times = [
    0.0005,
    0.0030,
    0.0080,
    0.0600,
    0.2200
]

plt.plot(
    sizes,
    times,
    marker='o'
)

plt.xlabel(
    "Number of Vertices"
)

plt.ylabel(
    "Execution Time (seconds)"
)

plt.title(
    "Ford-Fulkerson Performance Analysis"
)

plt.grid(True)

# Save the plot for the manual/document
plt.savefig("MaxFlow_Performance.png")
plt.show()
