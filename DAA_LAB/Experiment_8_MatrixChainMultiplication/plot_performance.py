import matplotlib.pyplot as plt
import time
import random
import os

try:
    from MatrixChain import matrix_chain_order
except ImportError:
    def matrix_chain_order(p, n, verbose=False):
        m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for L in range(2, n + 1):
            for i in range(1, n - L + 2):
                j = i + L - 1
                m[i][j] = float('inf')
                for k in range(i, j):
                    q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                    if q < m[i][j]:
                        m[i][j] = q
        return m[1][n]

def plot_performance():
    sizes = [10, 25, 50, 100, 200, 400]
    times = []

    print("Generating performance data for Matrix Chain DP O(N^3). This may take a few seconds...")
    
    for n in sizes:
        p = [random.randint(1, 100) for _ in range(n + 1)]
        
        start_time = time.time()
        matrix_chain_order(p, n)
        end_time = time.time()
        
        time_taken = end_time - start_time
        times.append(time_taken)
        print(f"Processed N = {n:<10} | Time = {time_taken:.6f} s")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', linestyle='-', color='red', linewidth=2, markersize=8)
    
    plt.title('Performance Analysis of MCM DP O(N^3)', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Number of Matrices (N)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    
    plt.xscale('log')
    plt.yscale('log') 
    plt.grid(True, which="both", ls="--", alpha=0.6)
    
    for i, txt in enumerate(times):
        plt.annotate(f"{txt:.4f}s", (sizes[i], times[i]), textcoords="offset points", xytext=(0,10), ha='center')

    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'MCM_Performance.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nGraph saved successfully to: {save_path}")

if __name__ == "__main__":
    plot_performance()
