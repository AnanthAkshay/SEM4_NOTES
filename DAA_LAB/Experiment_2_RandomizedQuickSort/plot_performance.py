import matplotlib.pyplot as plt
import time
import random
import os
import sys

# Increase recursion depth for sorting large arrays
sys.setrecursionlimit(200000)

try:
    from QuickSort import randomized_quick_sort
except ImportError:
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def randomized_partition(arr, low, high):
        random_idx = random.randint(low, high)
        arr[random_idx], arr[high] = arr[high], arr[random_idx]
        return partition(arr, low, high)

    def randomized_quick_sort(arr, low, high):
        if low < high:
            pi = randomized_partition(arr, low, high)
            randomized_quick_sort(arr, low, pi - 1)
            randomized_quick_sort(arr, pi + 1, high)

def plot_performance():
    sizes = [1, 10, 100, 1000, 10000, 100000]
    times = []

    print("Generating performance data. This may take a few seconds...")
    
    for n in sizes:
        arr = [random.randint(1, 1000000) for _ in range(n)]
        
        start_time = time.time()
        randomized_quick_sort(arr, 0, n - 1)
        end_time = time.time()
        
        time_taken = end_time - start_time
        times.append(time_taken)
        print(f"Processed N = {n:<10} | Time = {time_taken:.6f} s")

    # Plotting the graph
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='s', linestyle='-', color='r', linewidth=2, markersize=8)
    
    plt.title('Performance Analysis of Randomized Quick Sort', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Input Size (N)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--", alpha=0.6)
    
    for i, txt in enumerate(times):
        plt.annotate(f"{txt:.4f}s", (sizes[i], times[i]), textcoords="offset points", xytext=(0,10), ha='center')

    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'RandomizedQuickSort_Performance.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nGraph saved successfully to: {save_path}")

if __name__ == "__main__":
    plot_performance()
