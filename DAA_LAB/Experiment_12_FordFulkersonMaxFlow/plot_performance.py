import matplotlib.pyplot as plt
import time
import random
import os

try:
    from MaxFlow import ford_fulkerson
except ImportError:
    INF = float('inf')
    def bfs(r_graph, s, t, parent):
        visited = [False] * len(r_graph)
        queue = [s]
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for v, val in enumerate(r_graph[u]):
                if not visited[v] and val > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        return True
        return False

    def ford_fulkerson(graph, s, t, verbose=False):
        r_graph = [row[:] for row in graph]
        parent = [-1] * len(graph)
        max_flow = 0
        while bfs(r_graph, s, t, parent):
            path_flow = INF
            curr = t
            while curr != s:
                prev = parent[curr]
                path_flow = min(path_flow, r_graph[prev][curr])
                curr = prev
            curr = t
            while curr != s:
                prev = parent[curr]
                r_graph[prev][curr] -= path_flow
                r_graph[curr][prev] += path_flow
                curr = prev
            max_flow += path_flow
        return max_flow

def plot_performance():
    sizes = [10, 30, 50, 80, 100, 150]
    times = []

    print("Generating performance data for Ford-Fulkerson Max Flow. This may take a few seconds...")
    
    for v in sizes:
        s = 0
        t = v - 1
        
        # Build random DAG flow graph
        graph = [[0] * v for _ in range(v)]
        for src in range(v - 1):
            num_edges = random.randint(2, 4)
            for _ in range(num_edges):
                dest = random.randint(src + 1, v - 1)
                graph[src][dest] = random.randint(10, 100)
                
        start_time = time.time()
        ford_fulkerson(graph, s, t, verbose=False)
        end_time = time.time()
        
        time_taken = end_time - start_time
        times.append(time_taken)
        print(f"Processed Vertices = {v:<10} | Time = {time_taken:.6f} s")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', linestyle='-', color='red', linewidth=2, markersize=8)
    
    plt.title('Performance Analysis of Ford-Fulkerson (Edmonds-Karp) Max Flow', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Number of Vertices (V)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    
    plt.grid(True, which="both", ls="--", alpha=0.6)
    
    for i, txt in enumerate(times):
        plt.annotate(f"{txt:.5f}s", (sizes[i], times[i]), textcoords="offset points", xytext=(0,10), ha='center')

    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'MaxFlow_Performance.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nGraph saved successfully to: {save_path}")

if __name__ == "__main__":
    plot_performance()
