#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_NODES 100
#define WHITE 0 // Unvisited
#define GRAY 1  // Visiting (in recursion stack)
#define BLACK 2 // Finished

// Node in adjacency list
struct AdjListNode {
    int dest;
    struct AdjListNode* next;
};

// Adjacency list representation
struct AdjList {
    struct AdjListNode* head;
};

// Graph representation
struct Graph {
    int numVertices;
    struct AdjList* array;
    char** nodeNames; // Directory/File names
};

// Create a new adjacency list node
struct AdjListNode* newAdjListNode(int dest) {
    struct AdjListNode* newNode = (struct AdjListNode*)malloc(sizeof(struct AdjListNode));
    newNode->dest = dest;
    newNode->next = NULL;
    return newNode;
}

// Create a graph of V vertices
struct Graph* createGraph(int V) {
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
    graph->numVertices = V;
    graph->array = (struct AdjList*)malloc(V * sizeof(struct AdjList));
    graph->nodeNames = (char**)malloc(V * sizeof(char*));
    for (int i = 0; i < V; ++i) {
        graph->array[i].head = NULL;
        graph->nodeNames[i] = (char*)malloc(50 * sizeof(char));
        sprintf(graph->nodeNames[i], "Node_%d", i);
    }
    return graph;
}

// Add edge to directed graph
void addEdge(struct Graph* graph, int src, int dest) {
    struct AdjListNode* newNode = newAdjListNode(dest);
    newNode->next = graph->array[src].head;
    graph->array[src].head = newNode;
}

// Variables for DFS
int dfsTime = 0;
int discoveryTime[MAX_NODES];
int finishingTime[MAX_NODES];
int color[MAX_NODES];
int parentNode[MAX_NODES];

// DFS Visit function with edge classification
void dfsVisit(struct Graph* graph, int u, int verbose) {
    color[u] = GRAY;
    discoveryTime[u] = ++dfsTime;
    
    if (verbose) {
        printf("Discover Node %d (%s) at t = %d\n", u, graph->nodeNames[u], discoveryTime[u]);
    }

    struct AdjListNode* temp = graph->array[u].head;
    while (temp != NULL) {
        int v = temp->dest;
        
        if (color[v] == WHITE) {
            parentNode[v] = u;
            if (verbose) {
                printf("  Edge (%s -> %s) is a TREE EDGE\n", graph->nodeNames[u], graph->nodeNames[v]);
            }
            dfsVisit(graph, v, verbose);
        } 
        else if (color[v] == GRAY) {
            if (verbose) {
                printf("  Edge (%s -> %s) is a BACK EDGE (Cycle Detected!)\n", graph->nodeNames[u], graph->nodeNames[v]);
            }
        } 
        else if (color[v] == BLACK) {
            if (discoveryTime[u] < discoveryTime[v]) {
                if (verbose) {
                    printf("  Edge (%s -> %s) is a FORWARD EDGE\n", graph->nodeNames[u], graph->nodeNames[v]);
                }
            } else {
                if (verbose) {
                    printf("  Edge (%s -> %s) is a CROSS EDGE\n", graph->nodeNames[u], graph->nodeNames[v]);
                }
            }
        }
        temp = temp->next;
    }

    color[u] = BLACK;
    finishingTime[u] = ++dfsTime;
    
    if (verbose) {
        printf("Finish Node %d (%s) at t = %d\n", u, graph->nodeNames[u], finishingTime[u]);
    }
}

// Main DFS runner
void runDFS(struct Graph* graph, int verbose) {
    dfsTime = 0;
    int V = graph->numVertices;
    
    for (int i = 0; i < V; i++) {
        color[i] = WHITE;
        parentNode[i] = -1;
        discoveryTime[i] = 0;
        finishingTime[i] = 0;
    }

    if (verbose) {
        printf("\n--- DFS Traversal & Edge Classification ---\n");
    }

    // Traverse all components
    for (int i = 0; i < V; i++) {
        if (color[i] == WHITE) {
            if (verbose) {
                printf("\nStarting DFS Tree from root component: %s\n", graph->nodeNames[i]);
            }
            dfsVisit(graph, i, verbose);
        }
    }
    
    if (verbose) {
        printf("\n--- Discovery and Finishing Times Table ---\n");
        printf("%-15s | %-15s | %-15s | %-15s\n", "Node ID", "Node Name", "Discovery (d)", "Finishing (f)");
        printf("-------------------------------------------------------------------\n");
        for (int i = 0; i < V; i++) {
            printf("%-15d | %-15s | %-15d | %-15d\n", i, graph->nodeNames[i], discoveryTime[i], finishingTime[i]);
        }
    }
}

// Setup a directory structure as a graph
struct Graph* setupDirectoryGraph() {
    // 8 vertices representing directories and files
    // 0: root, 1: src, 2: include, 3: bin, 4: main.c, 5: utils.c, 6: utils.h, 7: build.log
    struct Graph* graph = createGraph(8);
    strcpy(graph->nodeNames[0], "root");
    strcpy(graph->nodeNames[1], "src");
    strcpy(graph->nodeNames[2], "include");
    strcpy(graph->nodeNames[3], "bin");
    strcpy(graph->nodeNames[4], "main.c");
    strcpy(graph->nodeNames[5], "utils.c");
    strcpy(graph->nodeNames[6], "utils.h");
    strcpy(graph->nodeNames[7], "build.log");

    // Edges modeling directory containment or dependency mapping:
    // root contains: src, include, bin, build.log
    addEdge(graph, 0, 1); // root -> src
    addEdge(graph, 0, 2); // root -> include
    addEdge(graph, 0, 3); // root -> bin
    addEdge(graph, 0, 7); // root -> build.log
    
    // src contains: main.c, utils.c
    addEdge(graph, 1, 4); // src -> main.c
    addEdge(graph, 1, 5); // src -> utils.c

    // include contains: utils.h
    addEdge(graph, 2, 6); // include -> utils.h

    // Dependencies: main.c includes utils.h, utils.c includes utils.h
    addEdge(graph, 4, 6); // main.c -> utils.h (dependency edge)
    addEdge(graph, 5, 6); // utils.c -> utils.h (dependency edge)
    
    // Cross edge simulation (e.g. main.c writes to build.log)
    addEdge(graph, 4, 7); // main.c -> build.log

    return graph;
}

// Free graph memory
void freeGraph(struct Graph* graph) {
    for (int i = 0; i < graph->numVertices; i++) {
        struct AdjListNode* temp = graph->array[i].head;
        while (temp != NULL) {
            struct AdjListNode* toFree = temp;
            temp = temp->next;
            free(toFree);
        }
        free(graph->nodeNames[i]);
    }
    free(graph->array);
    free(graph->nodeNames);
    free(graph);
}

// Performance analysis with random graph DFS
void performanceAnalysis() {
    int sizes[] = {100, 500, 1000, 5000, 10000, 20000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    printf("\n--- Performance Analysis (DFS Traversal: O(V + E)) ---\n");
    printf("%-20s | %-20s | %-20s\n", "Vertices (V)", "Edges (E = 3*V)", "Time Taken (seconds)");
    printf("-------------------------------------------------------------\n");

    for (int i = 0; i < num_sizes; i++) {
        int v = sizes[i];
        int e = v * 3;
        struct Graph* graph = createGraph(v);
        
        // Add random edges
        for (int j = 0; j < e; j++) {
            int src = rand() % v;
            int dest = rand() % v;
            if (src != dest) {
                addEdge(graph, src, dest);
            }
        }

        // Run DFS and time it
        // We override discovery and finishing time arrays sizes for this performance test
        // By allocating them dynamically or just bounding them in the test since V can exceed MAX_NODES
        int* tempColor = (int*)malloc(v * sizeof(int));
        int* tempParent = (int*)malloc(v * sizeof(int));
        int* tempDiscovery = (int*)malloc(v * sizeof(int));
        int* tempFinishing = (int*)malloc(v * sizeof(int));

        clock_t start = clock();
        
        // Local DFS implementation to support huge graph sizes dynamically
        int localTime = 0;
        for (int j = 0; j < v; j++) {
            tempColor[j] = WHITE;
            tempParent[j] = -1;
            tempDiscovery[j] = 0;
            tempFinishing[j] = 0;
        }

        // Inner function simulation using a stack or simply a recursive helper with dynamic arrays
        // Since C doesn't easily support nested functions with access to locals, we can define a small stack DFS 
        // to prevent deep recursive call overflow for V = 20000.
        // Let's implement recursive helper that receives dynamic array pointers.
        void localDfsVisit(struct Graph* g, int node, int* time_ptr, int* col, int* disc, int* fin) {
            col[node] = GRAY;
            (*time_ptr)++;
            disc[node] = *time_ptr;
            struct AdjListNode* temp = g->array[node].head;
            while (temp != NULL) {
                int neighbor = temp->dest;
                if (col[neighbor] == WHITE) {
                    localDfsVisit(g, neighbor, time_ptr, col, disc, fin);
                }
                temp = temp->next;
            }
            col[node] = BLACK;
            (*time_ptr)++;
            fin[node] = *time_ptr;
        }

        for (int j = 0; j < v; j++) {
            if (tempColor[j] == WHITE) {
                localDfsVisit(graph, j, &localTime, tempColor, tempDiscovery, tempFinishing);
            }
        }

        clock_t end = clock();
        double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        
        printf("%-20d | %-20d | %-20f\n", v, e, time_taken);

        free(tempColor);
        free(tempParent);
        free(tempDiscovery);
        free(tempFinishing);
        freeGraph(graph);
    }
    printf("-------------------------------------------------------------\n");
}

int main() {
    int choice;
    srand(time(0));

    while (1) {
        printf("\n=========================================\n");
        printf(" FILE SYSTEM DIRECTORY MAPPER (DFS)      \n");
        printf("=========================================\n");
        printf("1. Map Directory and Record DFS Timestamps\n");
        printf("2. Run Performance Analysis\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        if (scanf("%d", &choice) != 1) break;

        switch (choice) {
            case 1: {
                struct Graph* graph = setupDirectoryGraph();
                runDFS(graph, 1); // verbose = 1
                freeGraph(graph);
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
