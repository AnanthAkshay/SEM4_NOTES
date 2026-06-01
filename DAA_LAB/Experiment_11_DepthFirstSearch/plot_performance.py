import matplotlib.pyplot as plt
import time
import random
import sys
import os

sys.setrecursionlimit(50000)

try:
    from DFS import Graph, dfs_visit
except ImportError:
    class Graph:
        def __init__(self, V):
            self.numVertices = V
            self.adjList = {i: [] for i in range(V)}
            self.nodeNames = {i: f"Node_{i}" for i in range(V)}
        def add_edge(self, src, dest):
            self.adjList[src].append(dest)

    def dfs_visit(graph, u, state, discovery_time, finishing_time, parent, time_counter, edge_types, verbose):
        state[u] = 1 # GRAY
        time_counter[0] += 1
        discovery_time[u] = time_counter[0]
        for v in graph.adjList[u]:
            if state[v] == 0:
                parent[v] = u
                dfs_visit(graph, v, state, discovery_time, finishing_time, parent, time_counter, edge_types, verbose)
        state[u] = 2 # BLACK
        time_counter[0] += 1
        finishing_time[u] = time_counter[0]

def plot_performance():
    sizes = [100, 500, 1000, 5000, 10000, 20000]
    times = []

    print("Generating performance data for DFS Traversal. This may take a few seconds...")
    
    for v in sizes:
        e = v * 3
        graph = Graph(v)
        
        # Populate random edges
        for _ in range(e):
            src = random.randint(0, v - 1)
            dest = random.randint(0, v - 1)
            if src != dest:
                graph.add_edge(src, dest)
                
        start_time = time.time()
        state = [0] * v
        discovery_time = [0] * v
        finishing_time = [0] * v
        parent = [-1] * v
        time_counter = [0]
        edge_types = []
        
        for i in range(v):
            if state[i] == 0:
                dfs_visit(graph, i, state, discovery_time, finishing_time, parent, time_counter, edge_types, verbose=False)
                
        end_time = time.time()
        time_taken = end_time - start_time
        times.append(time_taken)
        print(f"Processed V = {v:<8} | E = {e:<8} | Time = {time_taken:.6f} s")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', linestyle='-', color='green', linewidth=2, markersize=8)
    
    plt.title('Performance Analysis of DFS Traversal O(V + E)', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Number of Vertices (V) [Edges E = 3*V]', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    
    plt.grid(True, which="both", ls="--", alpha=0.6)
    
    for i, txt in enumerate(times):
        plt.annotate(f"{txt:.5f}s", (sizes[i], times[i]), textcoords="offset points", xytext=(0,10), ha='center')

    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DFS_Performance.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nGraph saved successfully to: {save_path}")

if __name__ == "__main__":
    plot_performance()
