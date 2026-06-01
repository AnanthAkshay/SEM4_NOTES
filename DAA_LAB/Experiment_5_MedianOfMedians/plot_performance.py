import matplotlib.pyplot as plt
import time
import random
import os
import sys

sys.setrecursionlimit(200000)

try:
    from MedianOfMedians import kth_smallest
except ImportError:
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def partition(arr, left, right, pivot_val):
        for i in range(left, right + 1):
            if arr[i] == pivot_val:
                arr[i], arr[right] = arr[right], arr[i]
                break
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        return i

    def kth_smallest(arr, left, right, k):
        if 0 < k <= right - left + 1:
            n = right - left + 1
            medians = []
            i = 0
            while i < n // 5:
                group = arr[left + i*5 : left + i*5 + 5]
                medians.append(insertion_sort(group)[2])
                i += 1
            if i * 5 < n:
                group = arr[left + i*5 : left + n]
                medians.append(insertion_sort(group)[len(group)//2])
                
            if len(medians) == 1:
                med_of_med = medians[0]
            else:
                med_of_med = kth_smallest(medians, 0, len(medians)-1, len(medians)//2 + 1)
                
            pos = partition(arr, left, right, med_of_med)
            
            if pos - left == k - 1:
                return arr[pos]
            if pos - left > k - 1:
                return kth_smallest(arr, left, pos - 1, k)
            return kth_smallest(arr, pos + 1, right, k - pos + left - 1)
        return -1

def plot_performance():
    sizes = [1, 10, 100, 1000, 10000, 100000]
    times = []

    print("Generating performance data for Median of Medians. This may take a few seconds...")
    
    for n in sizes:
        arr = [random.randint(1, 10000) for _ in range(n)]
        k = n // 2 + 1
        
        start_time = time.time()
        kth_smallest(arr, 0, n - 1, k)
        end_time = time.time()
        
        time_taken = end_time - start_time
        times.append(time_taken)
        print(f"Processed N = {n:<10} | Time = {time_taken:.6f} s")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='d', linestyle='-', color='teal', linewidth=2, markersize=8)
    
    plt.title('Performance Analysis of Median of Medians (Deterministic O(N))', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Input Size (N)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    
    plt.xscale('log')
    plt.yscale('log') 
    plt.grid(True, which="both", ls="--", alpha=0.6)
    
    for i, txt in enumerate(times):
        plt.annotate(f"{txt:.4f}s", (sizes[i], times[i]), textcoords="offset points", xytext=(0,10), ha='center')

    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'MedianOfMedians_Performance.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nGraph saved successfully to: {save_path}")

if __name__ == "__main__":
    plot_performance()
