import matplotlib.pyplot as plt
import time
import random
import os

# Import the merge_sort function from MergeSort.py
# Since it's in the same directory, we can import it directly
try:
    from MergeSort import merge_sort
except ImportError:
    # Fallback definition if import fails
    def merge(arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        L = arr[left:mid+1]
        R = arr[mid+1:right+1]
        i = j = 0
        k = left
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort(arr, left, right):
        if left < right:
            mid = left + (right - left) // 2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid + 1, right)
            merge(arr, left, mid, right)

def plot_performance():
    sizes = [1, 10, 100, 1000, 10000, 100000]
    times = []

    print("Generating performance data. This may take a few seconds...")
    
    for n in sizes:
        # Generate random array for testing
        arr = [random.randint(1, 1000000) for _ in range(n)]
        
        start_time = time.time()
        merge_sort(arr, 0, n - 1)
        end_time = time.time()
        
        time_taken = end_time - start_time
        times.append(time_taken)
        print(f"Processed N = {n:<10} | Time = {time_taken:.6f} s")

    # Plotting the graph
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', linestyle='-', color='b', linewidth=2, markersize=8)
    
    # Adding titles and labels
    plt.title('Performance Analysis of Merge Sort', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Input Size (N)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    
    # Setting x-axis to logarithmic scale for better visualization of N values
    plt.xscale('log')
    plt.yscale('log') # Log scale for y-axis too, as O(N log N) grows fast
    plt.grid(True, which="both", ls="--", alpha=0.6)
    
    # Annotate points
    for i, txt in enumerate(times):
        plt.annotate(f"{txt:.4f}s", (sizes[i], times[i]), textcoords="offset points", xytext=(0,10), ha='center')

    # Save the plot
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'MergeSort_Performance.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nGraph saved successfully to: {save_path}")
    
    # Display the plot if running interactively
    # plt.show() # Commented out to prevent blocking in automated environments

if __name__ == "__main__":
    plot_performance()
