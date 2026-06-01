import time
import random
import heapq
import sys

def dijkstra(graph, V, src):
    # dist array holds the shortest distance from src to i
    dist = [float('inf')] * V
    dist[src] = 0
    
    # Priority queue stores (distance, vertex)
    pq = [(0, src)]
    
    while pq:
        # Get the vertex with the minimum distance
        current_dist, u = heapq.heappop(pq)
        
        # If we found a longer path, ignore it
        if current_dist > dist[u]:
            continue
            
        # Explore neighbors
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
                
    return dist

def performance_analysis():
    sizes = [10, 100, 1000, 10000]
    
    print("\n--- Performance Analysis (Dijkstra using Min-Heap) ---")
    print(f"{'Vertices':<10} | {'Edges':<10} | {'Time Taken (seconds)':<20}")
    print("-" * 46)
    
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
        print(f"{V:<10} | {E:<10} | {time_taken:<20.6f}")
    print("-" * 46)

def main():
    while True:
        print("\n=========================================")
        print(" CITY NAVIGATION (DIJKSTRA SHORTEST PATH)")
        print("=========================================")
        print("1. Calculate Shortest Paths (Custom Graph)")
        print("2. Run Performance Analysis")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                V = int(input("Enter number of intersections (Vertices): "))
                E = int(input("Enter number of roads (Edges): "))
                
                graph = {i: [] for i in range(V)}
                print("Enter Edges as: Source Destination Weight")
                for _ in range(E):
                    u, v, w = map(int, input().split())
                    graph[u].append((v, w))
                    graph[v].append((u, w))
                    
                src = int(input("Enter Source Intersection: "))
                
                print(f"\nCalculating Shortest Paths from Source {src}...")
                distances = dijkstra(graph, V, src)
                
                print("Intersection\t Distance from Source")
                for i in range(V):
                    dist_str = "INF" if distances[i] == float('inf') else str(distances[i])
                    print(f"{i}\t\t {dist_str}")
                    
            except ValueError:
                print("Invalid input! Please enter integers.")
                
        elif choice == '2':
            performance_analysis()
            
        elif choice == '3':
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
