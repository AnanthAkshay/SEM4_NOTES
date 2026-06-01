#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_VERTICES 100
#define INF 1e9

// BFS helper to find an augmenting path in the residual graph
// Returns 1 if there is a path from source to sink, also stores the path in parent[]
int bfs(int rGraph[MAX_VERTICES][MAX_VERTICES], int V, int s, int t, int parent[]) {
    int visited[MAX_VERTICES] = {0};
    int queue[MAX_VERTICES];
    int front = 0, rear = 0;

    queue[rear++] = s;
    visited[s] = 1;
    parent[s] = -1;

    while (front < rear) {
        int u = queue[front++];

        for (int v = 0; v < V; v++) {
            if (!visited[v] && rGraph[u][v] > 0) {
                // If we find a connection to the sink node, then we
                // set its parent and return true
                if (v == t) {
                    parent[v] = u;
                    return 1;
                }
                queue[rear++] = v;
                parent[v] = u;
                visited[v] = 1;
            }
        }
    }

    return 0; // No augmenting path found
}

// Ford-Fulkerson / Edmonds-Karp Max Flow algorithm
int fordFulkerson(int graph[MAX_VERTICES][MAX_VERTICES], int V, int s, int t, int verbose) {
    int u, v;

    // Create a residual graph and fill the residual graph with
    // given capacities in the original graph as residual capacities
    int rGraph[MAX_VERTICES][MAX_VERTICES];
    for (u = 0; u < V; u++) {
        for (v = 0; v < V; v++) {
            rGraph[u][v] = graph[u][v];
        }
    }

    int parent[MAX_VERTICES]; // Filled by BFS to store the path
    int max_flow = 0;         // There is no flow initially

    if (verbose) {
        printf("\n--- Tracking Augmenting Paths ---\n");
    }

    // Augment the flow while there is a path from source to sink
    int path_count = 0;
    while (bfs(rGraph, V, s, t, parent)) {
        // Find minimum residual capacity of the edges along the path filled by BFS.
        // Or we can say find the maximum flow through the path found.
        int path_flow = INF;
        for (v = t; v != s; v = parent[v]) {
            u = parent[v];
            if (rGraph[u][v] < path_flow) {
                path_flow = rGraph[u][v];
            }
        }

        // Print the path and its bottleneck capacity
        if (verbose) {
            path_count++;
            printf("Path %d: ", path_count);
            
            // Reconstruct path for printing
            int path[MAX_VERTICES];
            int idx = 0;
            for (int curr = t; curr != -1; curr = parent[curr]) {
                path[idx++] = curr;
            }
            for (int i = idx - 1; i >= 0; i--) {
                printf("%d", path[i]);
                if (i > 0) printf(" -> ");
            }
            printf(" | Bottleneck Capacity = %d\n", path_flow);
        }

        // Update residual capacities of the edges and reverse edges along the path
        for (v = t; v != s; v = parent[v]) {
            u = parent[v];
            rGraph[u][v] -= path_flow;
            rGraph[v][u] += path_flow;
        }

        // Add path flow to overall flow
        max_flow += path_flow;
    }

    if (verbose) {
        printf("\nNo more augmenting paths found in residual graph.\n");
    }

    return max_flow;
}

// Function to run performance benchmarks on random flow networks
void performanceAnalysis() {
    int sizes[] = {10, 30, 50, 80, 100, 150};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    printf("\n--- Performance Analysis (Ford-Fulkerson / Edmonds-Karp: O(V * E^2)) ---\n");
    printf("%-20s | %-20s\n", "Vertices (V)", "Time Taken (seconds)");
    printf("---------------------------------------------\n");

    // Allocate adjacency matrix dynamically to avoid huge stack size issues
    for (int i = 0; i < num_sizes; i++) {
        int v = sizes[i];
        int s = 0;
        int t = v - 1;

        // Allocate local graph
        int **localGraph = (int **)malloc(v * sizeof(int *));
        for (int r = 0; r < v; r++) {
            localGraph[r] = (int *)malloc(v * sizeof(int));
            memset(localGraph[r], 0, v * sizeof(int));
        }

        // Build a random flow network where each node has a few random outgoing edges
        // Connect nodes to ensure path from source to sink
        for (int src = 0; src < v - 1; src++) {
            int num_edges = 2 + rand() % 3; // 2 to 4 edges per node
            for (int k = 0; k < num_edges; k++) {
                int dest = src + 1 + rand() % (v - src - 1); // Only forward edges to prevent infinite augmentation loops in benchmark
                localGraph[src][dest] = 10 + rand() % 90; // Capacity 10 to 100
            }
        }

        clock_t start = clock();

        // Local Edmonds-Karp running directly
        int rGraph[MAX_VERTICES][MAX_VERTICES];
        for (int r = 0; r < v && r < MAX_VERTICES; r++) {
            for (int col = 0; col < v && col < MAX_VERTICES; col++) {
                rGraph[r][col] = localGraph[r][col];
            }
        }

        int parent[MAX_VERTICES];
        int max_flow = 0;
        
        // Helper BFS inside loop
        int local_bfs(int rg[MAX_VERTICES][MAX_VERTICES], int nv, int src, int snk, int par[]) {
            int vis[MAX_VERTICES] = {0};
            int q[MAX_VERTICES];
            int f = 0, re = 0;
            q[re++] = src;
            vis[src] = 1;
            par[src] = -1;
            while (f < re) {
                int curr = q[f++];
                for (int next = 0; next < nv; next++) {
                    if (!vis[next] && rg[curr][next] > 0) {
                        if (next == snk) {
                            par[next] = curr;
                            return 1;
                        }
                        q[re++] = next;
                        par[next] = curr;
                        vis[next] = 1;
                    }
                }
            }
            return 0;
        }

        while (local_bfs(rGraph, v < MAX_VERTICES ? v : MAX_VERTICES, s, t, parent)) {
            int path_flow = INF;
            for (int curr = t; curr != s; curr = parent[curr]) {
                int prev = parent[curr];
                if (rGraph[prev][curr] < path_flow) {
                    path_flow = rGraph[prev][curr];
                }
            }
            for (int curr = t; curr != s; curr = parent[curr]) {
                int prev = parent[curr];
                rGraph[prev][curr] -= path_flow;
                rGraph[curr][prev] += path_flow;
            }
            max_flow += path_flow;
        }

        clock_t end = clock();
        double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

        printf("%-20d | %-20f\n", v, time_taken);

        for (int r = 0; r < v; r++) {
            free(localGraph[r]);
        }
        free(localGraph);
    }
    printf("---------------------------------------------\n");
}

int main() {
    int choice;
    srand(time(0));

    // Standard Edmonds-Karp network (6 nodes)
    // 0: S, 1: A, 2: B, 3: C, 4: D, 5: T
    int graph[MAX_VERTICES][MAX_VERTICES];
    memset(graph, 0, sizeof(graph));

    // Configure standard network
    graph[0][1] = 16; // S -> A
    graph[0][2] = 13; // S -> B
    graph[1][2] = 10; // A -> B
    graph[1][3] = 12; // A -> C
    graph[2][1] = 4;  // B -> A
    graph[2][4] = 14; // B -> D
    graph[3][2] = 9;  // C -> B
    graph[3][5] = 20; // C -> T
    graph[4][3] = 7;  // D -> C
    graph[4][5] = 4;  // D -> T

    while (1) {
        printf("\n=========================================\n");
        printf(" WATER DISTRIBUTION FLOW MAPPER (FF)     \n");
        printf("=========================================\n");
        printf("1. Compute Maximum Water Flow (6-Node Sample)\n");
        printf("2. Run Performance Analysis\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        if (scanf("%d", &choice) != 1) break;

        switch (choice) {
            case 1: {
                printf("\nOriginal Capacity Graph Configuration:\n");
                printf("  S -> A: 16 | S -> B: 13\n");
                printf("  A -> B: 10 | A -> C: 12\n");
                printf("  B -> A: 4  | B -> D: 14\n");
                printf("  C -> B: 9  | C -> T: 20\n");
                printf("  D -> C: 7  | D -> T: 4\n");
                
                int maxFlow = fordFulkerson(graph, 6, 0, 5, 1); // verbose = 1
                printf("\nMaximum Water Flow from Reservoir (S) to Zone (T) = %d liters/sec\n", maxFlow);
                break;
            }
            case 2:
                performanceAnalysis();
                break;
            case 3:
                printf("Exiting program...\n");
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }
    return 0;
}
