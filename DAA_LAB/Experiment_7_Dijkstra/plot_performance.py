import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]

times = [
    0.0004,
    0.0015,
    0.0038,
    0.0200,
    0.0450
]

plt.plot(sizes, times, marker='o')

plt.xlabel("Number of Vertices (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Dijkstra Algorithm Performance")

plt.grid(True)

# Save the plot for the manual/document
plt.savefig("Dijkstra_Performance.png")
plt.show()
