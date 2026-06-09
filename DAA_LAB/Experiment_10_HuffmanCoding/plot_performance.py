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
    0.0010,
    0.0060,
    0.0150
]

plt.plot(
    sizes,
    times,
    marker='o'
)

plt.xlabel(
    "Number of Characters"
)

plt.ylabel(
    "Execution Time (seconds)"
)

plt.title(
    "Huffman Coding Performance"
)

plt.grid(True)

# Save the plot for the manual/document
plt.savefig("Huffman_Performance.png")
plt.show()
