import time
import random
import sys

# Capacity network size limit
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

def ford_fulkerson(graph, s, t, verbose=True):
    # Create a residual graph and fill the residual graph with
    # given capacities in the original graph as residual capacities
    r_graph = [row[:] for row in graph]
    parent = [-1] * len(graph)
    max_flow = 0
    path_count = 0

    if verbose:
        print("\n--- Tracking Augmenting Paths ---")

    # Augment the flow while there is a path from source to sink
    while bfs(r_graph, s, t, parent):
        # Find minimum residual capacity of the edges along the path filled by BFS.
        path_flow = INF
        curr = t
        while curr != s:
            prev = parent[curr]
            path_flow = min(path_flow, r_graph[prev][curr])
            curr = prev

        # Print path and bottleneck capacity
        if verbose:
            path_count += 1
            path = []
            curr = t
            while curr != -1:
                path.append(curr)
                curr = parent[curr]
            path.reverse()
            path_str = " -> ".join(map(str, path))
            print(f"Path {path_count}: {path_str} | Bottleneck Capacity = {path_flow}")

        # Update residual capacities of the edges and reverse edges along the path
        curr = t
        while curr != s:
            prev = parent[curr]
            r_graph[prev][curr] -= path_flow
            r_graph[curr][prev] += path_flow
            curr = prev

        max_flow += path_flow

    if verbose:
        print("\nNo more augmenting paths found in residual graph.")

    return max_flow

def setup_standard_network():
    # 6 nodes: 0: S, 1: A, 2: B, 3: C, 4: D, 5: T
    n = 6
    graph = [[0] * n for _ in range(n)]

    graph[0][1] = 16 # S -> A
    graph[0][2] = 13 # S -> B
    graph[1][2] = 10 # A -> B
    graph[1][3] = 12 # A -> C
    graph[2][1] = 4  # B -> A
    graph[2][4] = 14 # B -> D
    graph[3][2] = 9  # C -> B
    graph[3][5] = 20 # C -> T
    graph[4][3] = 7  # D -> C
    graph[4][5] = 4  # D -> T

    return graph

def performance_analysis():
    sizes = [10, 30, 50, 80, 100, 150]
    
    print("\n--- Performance Analysis (Ford-Fulkerson / Edmonds-Karp: O(V * E^2)) ---")
    print(f"{'Vertices (V)':<15} | {'Time Taken (seconds)':<20}")
    print("-" * 40)
    
    for v in sizes:
        s = 0
        t = v - 1
        
        # Build random DAG flow graph to prevent infinite augmentation loop in benchmark
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
        print(f"{v:<15} | {time_taken:<20.6f}")
    print("-" * 40)

def main():
    while True:
        print("\n=========================================")
        print(" WATER DISTRIBUTION FLOW MAPPER (FF)     ")
        print("=========================================")
        print("1. Compute Maximum Water Flow (6-Node Sample)")
        print("2. Run Performance Analysis")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            graph = setup_standard_network()
            print("\nOriginal Capacity Graph Configuration:")
            print("  S -> A: 16 | S -> B: 13")
            print("  A -> B: 10 | A -> C: 12")
            print("  B -> A: 4  | B -> D: 14")
            print("  C -> B: 9  | C -> T: 20")
            print("  D -> C: 7  | D -> T: 4")
            
            max_flow = ford_fulkerson(graph, 0, 5, verbose=True)
            print(f"\nMaximum Water Flow from Reservoir (S) to Zone (T) = {max_flow} liters/sec")
            
        elif choice == '2':
            performance_analysis()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
