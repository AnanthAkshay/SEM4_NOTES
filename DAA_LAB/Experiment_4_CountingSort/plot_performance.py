import matplotlib.pyplot as plt
import time
import random
import os

try:
    from CountingSort import counting_sort, MAX_MARK
except ImportError:
    MAX_MARK = 100
    def counting_sort(arr):
        n = len(arr)
        output = [0] * n
        count = [0] * (MAX_MARK + 1)
        for i in range(n):
            count[arr[i]] += 1
        for i in range(1, MAX_MARK + 1):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            output[count[arr[i]] - 1] = arr[i]
            count[arr[i]] -= 1
            i -= 1
        for i in range(n):
            arr[i] = output[i]
        return arr

def plot_performance():
    sizes = [1, 10, 100, 1000, 10000, 100000]
    times = []

    print("Generating performance data for Counting Sort. This may take a few seconds...")
    
    for n in sizes:
        arr = [random.randint(0, MAX_MARK) for _ in range(n)]
        
        start_time = time.time()
        counting_sort(arr)
        end_time = time.time()
        
        time_taken = end_time - start_time
        times.append(time_taken)
        print(f"Processed N = {n:<10} | Time = {time_taken:.6f} s")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', linestyle='-', color='purple', linewidth=2, markersize=8)
    
    plt.title('Performance Analysis of Counting Sort O(N+K)', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Input Size (N)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    
    plt.xscale('log')
    # Use linear scale for Y since O(N) is linear, but since X is log, we can leave Y as log to see the straight line
    plt.yscale('log') 
    plt.grid(True, which="both", ls="--", alpha=0.6)
    
    for i, txt in enumerate(times):
        plt.annotate(f"{txt:.4f}s", (sizes[i], times[i]), textcoords="offset points", xytext=(0,10), ha='center')

    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'CountingSort_Performance.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nGraph saved successfully to: {save_path}")

if __name__ == "__main__":
    plot_performance()
