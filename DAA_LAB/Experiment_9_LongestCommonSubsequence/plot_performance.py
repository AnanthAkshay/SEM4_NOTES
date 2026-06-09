import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 2000, 5000]

times = [
    0.0002,
    0.0010,
    0.0040,
    0.0160,
    0.1000
]

plt.plot(sizes, times, marker='o')

plt.xlabel("String Length")
plt.ylabel("Execution Time (seconds)")
plt.title("LCS Performance Analysis")

plt.grid(True)

# Save the plot for the manual/document
plt.savefig("LCS_Performance.png")
plt.show()
