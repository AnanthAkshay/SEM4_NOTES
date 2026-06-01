import matplotlib.pyplot as plt
import time
import random
import os

try:
    from PriorityQueue import MaxHeap
except ImportError:
    class MaxHeap:
        def __init__(self):
            self.heap = []
        def parent(self, i): return (i - 1) // 2
        def left_child(self, i): return 2 * i + 1
        def right_child(self, i): return 2 * i + 2
        def insert(self, key):
            self.heap.append(key)
            self._heapify_up(len(self.heap) - 1)
        def _heapify_up(self, i):
            while i != 0 and self.heap[self.parent(i)] < self.heap[i]:
                self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
                i = self.parent(i)
        def extract_max(self):
            if len(self.heap) == 0: return None
            if len(self.heap) == 1: return self.heap.pop()
            root = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._heapify_down(0)
            return root
        def _heapify_down(self, i):
            largest = i
            left = self.left_child(i)
            right = self.right_child(i)
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                self._heapify_down(largest)

def plot_performance():
    sizes = [1, 10, 100, 1000, 10000, 100000]
    times = []

    print("Generating performance data (Extract Max). This may take a few seconds...")
    
    for n in sizes:
        pq = MaxHeap()
        # Insert N elements
        for _ in range(n):
            pq.insert(random.randint(1, 1000000))
            
        # Measure time taken to extract max N times
        start_time = time.time()
        for _ in range(n):
            pq.extract_max()
        end_time = time.time()
        
        time_taken = end_time - start_time
        times.append(time_taken)
        print(f"Processed N = {n:<10} | Time = {time_taken:.6f} s")

    # Plotting the graph
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='^', linestyle='-', color='g', linewidth=2, markersize=8)
    
    plt.title('Performance Analysis of Priority Queue (Extract Max N times)', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Input Size (N)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--", alpha=0.6)
    
    for i, txt in enumerate(times):
        plt.annotate(f"{txt:.4f}s", (sizes[i], times[i]), textcoords="offset points", xytext=(0,10), ha='center')

    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'PriorityQueue_Performance.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nGraph saved successfully to: {save_path}")

if __name__ == "__main__":
    plot_performance()
