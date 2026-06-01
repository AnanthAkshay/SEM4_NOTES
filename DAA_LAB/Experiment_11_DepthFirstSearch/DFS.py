import time
import random
import sys

# Set recursion limit higher just in case of large deep graphs
sys.setrecursionlimit(50000)

class Graph:
    def __init__(self, V):
        self.numVertices = V
        self.adjList = {i: [] for i in range(V)}
        self.nodeNames = {i: f"Node_{i}" for i in range(V)}

    def add_edge(self, src, dest):
        self.adjList[src].append(dest)

def dfs_visit(graph, u, state, discovery_time, finishing_time, parent, time_counter, edge_types, verbose):
    # WHITE = 0, GRAY = 1, BLACK = 2
    state[u] = 1 # GRAY
    time_counter[0] += 1
    discovery_time[u] = time_counter[0]
    
    if verbose:
        print(f"Discover Node {u} ({graph.nodeNames[u]}) at t = {discovery_time[u]}")

    for v in graph.adjList[u]:
        if state[v] == 0: # WHITE
            parent[v] = u
            edge_types.append((u, v, "TREE EDGE"))
            if verbose:
                print(f"  Edge ({graph.nodeNames[u]} -> {graph.nodeNames[v]}) is a TREE EDGE")
            dfs_visit(graph, v, state, discovery_time, finishing_time, parent, time_counter, edge_types, verbose)
        elif state[v] == 1: # GRAY
            edge_types.append((u, v, "BACK EDGE"))
            if verbose:
                print(f"  Edge ({graph.nodeNames[u]} -> {graph.nodeNames[v]}) is a BACK EDGE (Cycle Detected!)")
        elif state[v] == 2: # BLACK
            if discovery_time[u] < discovery_time[v]:
                edge_types.append((u, v, "FORWARD EDGE"))
                if verbose:
                    print(f"  Edge ({graph.nodeNames[u]} -> {graph.nodeNames[v]}) is a FORWARD EDGE")
            else:
                edge_types.append((u, v, "CROSS EDGE"))
                if verbose:
                    print(f"  Edge ({graph.nodeNames[u]} -> {graph.nodeNames[v]}) is a CROSS EDGE")

    state[u] = 2 # BLACK
    time_counter[0] += 1
    finishing_time[u] = time_counter[0]
    
    if verbose:
        print(f"Finish Node {u} ({graph.nodeNames[u]}) at t = {finishing_time[u]}")

def run_dfs(graph, verbose=True):
    V = graph.numVertices
    state = [0] * V # 0: WHITE, 1: GRAY, 2: BLACK
    discovery_time = [0] * V
    finishing_time = [0] * V
    parent = [-1] * V
    time_counter = [0]
    edge_types = []

    if verbose:
        print("\n--- DFS Traversal & Edge Classification ---")

    for i in range(V):
        if state[i] == 0:
            if verbose:
                print(f"\nStarting DFS Tree from root component: {graph.nodeNames[i]}")
            dfs_visit(graph, i, state, discovery_time, finishing_time, parent, time_counter, edge_types, verbose)

    if verbose:
        print("\n--- Discovery and Finishing Times Table ---")
        print(f"{'Node ID':<10} | {'Node Name':<15} | {'Discovery (d)':<15} | {'Finishing (f)':<15}")
        print("-" * 65)
        for i in range(V):
            print(f"{i:<10} | {graph.nodeNames[i]:<15} | {discovery_time[i]:<15} | {finishing_time[i]:<15}")

    return discovery_time, finishing_time, edge_types

def setup_directory_graph():
    # 8 nodes representing directory tree
    graph = Graph(8)
    graph.nodeNames = {
        0: "root",
        1: "src",
        2: "include",
        3: "bin",
        4: "main.c",
        5: "utils.c",
        6: "utils.h",
        7: "build.log"
    }

    # Add containment and dependency edges
    graph.add_edge(0, 1) # root -> src
    graph.add_edge(0, 2) # root -> include
    graph.add_edge(0, 3) # root -> bin
    graph.add_edge(0, 7) # root -> build.log
    
    graph.add_edge(1, 4) # src -> main.c
    graph.add_edge(1, 5) # src -> utils.c

    graph.add_edge(2, 6) # include -> utils.h

    graph.add_edge(4, 6) # main.c -> utils.h (dependency)
    graph.add_edge(5, 6) # utils.c -> utils.h (dependency)
    
    graph.add_edge(4, 7) # main.c -> build.log (cross edge)

    return graph

def performance_analysis():
    sizes = [100, 500, 1000, 5000, 10000, 20000]
    
    print("\n--- Performance Analysis (DFS Traversal: O(V + E)) ---")
    print(f"{'Vertices (V)':<15} | {'Edges (E = 3*V)':<15} | {'Time Taken (seconds)':<20}")
    print("-" * 55)
    
    for v in sizes:
        e = v * 3
        graph = Graph(v)
        
        # Populate random edges
        for _ in range(e):
            src = random.randint(0, v - 1)
            dest = random.randint(0, v - 1)
            if src != dest:
                graph.add_edge(src, dest)
                
        # Run DFS and measure time
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
        print(f"{v:<15} | {e:<15} | {time_taken:<20.6f}")
    print("-" * 55)

def main():
    while True:
        print("\n=========================================")
        print(" FILE SYSTEM DIRECTORY MAPPER (DFS)      ")
        print("=========================================")
        print("1. Map Directory and Record DFS Timestamps")
        print("2. Run Performance Analysis")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            graph = setup_directory_graph()
            run_dfs(graph, verbose=True)
        elif choice == '2':
            performance_analysis()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
