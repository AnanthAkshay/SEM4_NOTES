import matplotlib.pyplot as plt
import time
import random
import os
import heapq

def dijkstra(graph, V, src):
    dist = [float('inf')] * V
    dist[src] = 0
    pq = [(0, src)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist

def plot_performance():
    sizes = [10, 100, 1000, 10000, 100000]
    times = []

    print("Generating performance data for Dijkstra O((V+E)log V). This may take a few seconds...")
    
    for V in sizes:
        E = V * 5 # Sparse graph
        
        # Build graph
        graph = {i: [] for i in range(V)}
        for _ in range(E):
            u = random.randint(0, V - 1)
            v = random.randint(0, V - 1)
            w = random.randint(1, 100)
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        start_time = time.time()
        dijkstra(graph, V, 0)
        end_time = time.time()
        
        time_taken = end_time - start_time
        times.append(time_taken)
        print(f"Processed V={V:<7} E={E:<8} | Time = {time_taken:.6f} s")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='^', linestyle='-', color='orange', linewidth=2, markersize=8)
    
    plt.title('Performance Analysis of Dijkstra O((V+E)log V)', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Number of Vertices (V)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    
    plt.xscale('log')
    plt.yscale('log') 
    plt.grid(True, which="both", ls="--", alpha=0.6)
    
    for i, txt in enumerate(times):
        plt.annotate(f"{txt:.4f}s", (sizes[i], times[i]), textcoords="offset points", xytext=(0,10), ha='center')

    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dijkstra_Performance.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nGraph saved successfully to: {save_path}")

if __name__ == "__main__":
    plot_performance()
