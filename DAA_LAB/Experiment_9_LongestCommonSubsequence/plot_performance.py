import matplotlib.pyplot as plt
import time
import random
import os

try:
    from LCS import lcs
except ImportError:
    def lcs(X, Y, verbose=False):
        m, n = len(X), len(Y)
        L = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif X[i - 1] == Y[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])
        return L[m][n]

def generate_random_string(length):
    return ''.join(random.choices("ACTG", k=length))

def plot_performance():
    sizes = [10, 100, 500, 1000, 2000]
    times = []

    print("Generating performance data for LCS DP O(M*N). This may take a few seconds...")
    
    for n in sizes:
        X = generate_random_string(n)
        Y = generate_random_string(n)
        
        start_time = time.time()
        lcs(X, Y)
        end_time = time.time()
        
        time_taken = end_time - start_time
        times.append(time_taken)
        print(f"Processed N = {n:<10} | Time = {time_taken:.6f} s")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', linestyle='-', color='blue', linewidth=2, markersize=8)
    
    plt.title('Performance Analysis of LCS DP O(M*N)', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('String Lengths (N)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    
    plt.xscale('log')
    plt.yscale('log') 
    plt.grid(True, which="both", ls="--", alpha=0.6)
    
    for i, txt in enumerate(times):
        plt.annotate(f"{txt:.4f}s", (sizes[i], times[i]), textcoords="offset points", xytext=(0,10), ha='center')

    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'LCS_Performance.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nGraph saved successfully to: {save_path}")

if __name__ == "__main__":
    plot_performance()
