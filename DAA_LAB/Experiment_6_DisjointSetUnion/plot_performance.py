import matplotlib.pyplot as plt
import time
import random
import os
import sys

sys.setrecursionlimit(200000)

try:
    from DisjointSetUnion import DSU
except ImportError:
    class DSU:
        def __init__(self, n):
            self.n = n
            self.parent = list(range(n))
            self.rank = [0] * n
        def find(self, i):
            if self.parent[i] != i:
                self.parent[i] = self.find(self.parent[i])
            return self.parent[i]
        def union(self, x, y):
            rootX = self.find(x)
            rootY = self.find(y)
            if rootX == rootY:
                return
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def plot_performance():
    sizes = [1, 10, 100, 1000, 10000, 100000]
    times = []

    print("Generating performance data for DSU (N Union Operations). This may take a few seconds...")
    
    for n in sizes:
        dsu = DSU(n)
        
        start_time = time.time()
        for _ in range(n):
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            dsu.union(u, v)
        end_time = time.time()
        
        time_taken = end_time - start_time
        times.append(time_taken)
        print(f"Processed N = {n:<10} | Time = {time_taken:.6f} s")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='s', linestyle='-', color='magenta', linewidth=2, markersize=8)
    
    plt.title('Performance Analysis of DSU (N Union Operations)', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Input Size (N users/operations)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    
    plt.xscale('log')
    plt.yscale('log') 
    plt.grid(True, which="both", ls="--", alpha=0.6)
    
    for i, txt in enumerate(times):
        plt.annotate(f"{txt:.4f}s", (sizes[i], times[i]), textcoords="offset points", xytext=(0,10), ha='center')

    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DSU_Performance.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nGraph saved successfully to: {save_path}")

if __name__ == "__main__":
    plot_performance()
