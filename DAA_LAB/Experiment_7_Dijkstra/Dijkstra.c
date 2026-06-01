#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

// Structure for Adjacency List Node
typedef struct AdjListNode {
    int dest;
    int weight;
    struct AdjListNode* next;
} AdjListNode;

// Structure for Adjacency List
typedef struct AdjList {
    AdjListNode *head;
} AdjList;

// Structure for Graph
typedef struct Graph {
    int V;
    AdjList *array;
} Graph;

// Create a new Adjacency List Node
AdjListNode* newAdjListNode(int dest, int weight) {
    AdjListNode* newNode = (AdjListNode*)malloc(sizeof(AdjListNode));
    newNode->dest = dest;
    newNode->weight = weight;
    newNode->next = NULL;
    return newNode;
}

// Create a Graph
Graph* createGraph(int V) {
    Graph* graph = (Graph*)malloc(sizeof(Graph));
    graph->V = V;
    graph->array = (AdjList*)malloc(V * sizeof(AdjList));
    for (int i = 0; i < V; ++i)
        graph->array[i].head = NULL;
    return graph;
}

// Add Edge (Undirected graph for city roads)
void addEdge(Graph* graph, int src, int dest, int weight) {
    AdjListNode* newNode = newAdjListNode(dest, weight);
    newNode->next = graph->array[src].head;
    graph->array[src].head = newNode;

    newNode = newAdjListNode(src, weight);
    newNode->next = graph->array[dest].head;
    graph->array[dest].head = newNode;
}

// Min Heap Node
typedef struct MinHeapNode {
    int v;
    int dist;
} MinHeapNode;

// Min Heap Structure
typedef struct MinHeap {
    int size;
    int capacity;
    int *pos;
    MinHeapNode **array;
} MinHeap;

MinHeapNode* newMinHeapNode(int v, int dist) {
    MinHeapNode* minHeapNode = (MinHeapNode*)malloc(sizeof(MinHeapNode));
    minHeapNode->v = v;
    minHeapNode->dist = dist;
    return minHeapNode;
}

MinHeap* createMinHeap(int capacity) {
    MinHeap* minHeap = (MinHeap*)malloc(sizeof(MinHeap));
    minHeap->pos = (int *)malloc(capacity * sizeof(int));
    minHeap->size = 0;
    minHeap->capacity = capacity;
    minHeap->array = (MinHeapNode**)malloc(capacity * sizeof(MinHeapNode*));
    return minHeap;
}

void swapMinHeapNode(MinHeapNode** a, MinHeapNode** b) {
    MinHeapNode* t = *a;
    *a = *b;
    *b = t;
}

void minHeapify(MinHeap* minHeap, int idx) {
    int smallest, left, right;
    smallest = idx;
    left = 2 * idx + 1;
    right = 2 * idx + 2;

    if (left < minHeap->size && minHeap->array[left]->dist < minHeap->array[smallest]->dist)
        smallest = left;

    if (right < minHeap->size && minHeap->array[right]->dist < minHeap->array[smallest]->dist)
        smallest = right;

    if (smallest != idx) {
        MinHeapNode *smallestNode = minHeap->array[smallest];
        MinHeapNode *idxNode = minHeap->array[idx];

        minHeap->pos[smallestNode->v] = idx;
        minHeap->pos[idxNode->v] = smallest;

        swapMinHeapNode(&minHeap->array[smallest], &minHeap->array[idx]);
        minHeapify(minHeap, smallest);
    }
}

int isEmpty(MinHeap* minHeap) {
    return minHeap->size == 0;
}

MinHeapNode* extractMin(MinHeap* minHeap) {
    if (isEmpty(minHeap))
        return NULL;

    MinHeapNode* root = minHeap->array[0];
    MinHeapNode* lastNode = minHeap->array[minHeap->size - 1];
    minHeap->array[0] = lastNode;

    minHeap->pos[root->v] = minHeap->size - 1;
    minHeap->pos[lastNode->v] = 0;

    --minHeap->size;
    minHeapify(minHeap, 0);

    return root;
}

void decreaseKey(MinHeap* minHeap, int v, int dist) {
    int i = minHeap->pos[v];
    minHeap->array[i]->dist = dist;

    while (i && minHeap->array[i]->dist < minHeap->array[(i - 1) / 2]->dist) {
        minHeap->pos[minHeap->array[i]->v] = (i - 1) / 2;
        minHeap->pos[minHeap->array[(i - 1) / 2]->v] = i;
        swapMinHeapNode(&minHeap->array[i], &minHeap->array[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}

int isInMinHeap(MinHeap *minHeap, int v) {
    if (minHeap->pos[v] < minHeap->size)
        return 1;
    return 0;
}

void printArr(int dist[], int n) {
    printf("Intersection\t Distance from Source\n");
    for (int i = 0; i < n; ++i)
        printf("%d \t\t %d\n", i, dist[i]);
}

void dijkstra(Graph* graph, int src, int verbose) {
    int V = graph->V;
    int *dist = (int *)malloc(V * sizeof(int));
    MinHeap* minHeap = createMinHeap(V);

    for (int v = 0; v < V; ++v) {
        dist[v] = INT_MAX;
        minHeap->array[v] = newMinHeapNode(v, dist[v]);
        minHeap->pos[v] = v;
    }

    minHeap->array[src] = newMinHeapNode(src, dist[src]);
    minHeap->pos[src] = src;
    dist[src] = 0;
    decreaseKey(minHeap, src, dist[src]);
    minHeap->size = V;

    while (!isEmpty(minHeap)) {
        MinHeapNode* minHeapNode = extractMin(minHeap);
        int u = minHeapNode->v;

        AdjListNode* pCrawl = graph->array[u].head;
        while (pCrawl != NULL) {
            int v = pCrawl->dest;
            if (isInMinHeap(minHeap, v) && dist[u] != INT_MAX && pCrawl->weight + dist[u] < dist[v]) {
                dist[v] = dist[u] + pCrawl->weight;
                decreaseKey(minHeap, v, dist[v]);
            }
            pCrawl = pCrawl->next;
        }
        free(minHeapNode);
    }
    
    if (verbose) {
        printArr(dist, V);
    }
    
    // Free memory
    free(minHeap->array);
    free(minHeap->pos);
    free(minHeap);
    free(dist);
}

void freeGraph(Graph* graph) {
    for (int i = 0; i < graph->V; i++) {
        AdjListNode* pCrawl = graph->array[i].head;
        while (pCrawl != NULL) {
            AdjListNode* temp = pCrawl;
            pCrawl = pCrawl->next;
            free(temp);
        }
    }
    free(graph->array);
    free(graph);
}

void performanceAnalysis() {
    int sizes[] = {10, 100, 1000, 10000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    printf("\n--- Performance Analysis (Dijkstra using Min-Heap) ---\n");
    printf("%-10s | %-10s | %-20s\n", "Vertices", "Edges", "Time Taken (seconds)");
    printf("----------------------------------------------\n");

    for (int i = 0; i < num_sizes; i++) {
        int V = sizes[i];
        int E = V * 5; // Sparse graph, average degree 10
        Graph* graph = createGraph(V);
        
        for (int j = 0; j < E; j++) {
            int u = rand() % V;
            int v = rand() % V;
            int w = (rand() % 100) + 1;
            addEdge(graph, u, v, w);
        }

        clock_t start = clock();
        dijkstra(graph, 0, 0); // verbose = 0
        clock_t end = clock();

        double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("%-10d | %-10d | %-20f\n", V, E, time_taken);
        freeGraph(graph);
    }
    printf("----------------------------------------------\n");
}

int main() {
    int choice;
    srand(time(0));

    while (1) {
        printf("\n=========================================\n");
        printf(" CITY NAVIGATION (DIJKSTRA SHORTEST PATH)\n");
        printf("=========================================\n");
        printf("1. Calculate Shortest Paths (Custom Graph)\n");
        printf("2. Run Performance Analysis\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        if (scanf("%d", &choice) != 1) break;

        switch (choice) {
            case 1: {
                int V, E;
                printf("Enter number of intersections (Vertices): ");
                scanf("%d", &V);
                printf("Enter number of roads (Edges): ");
                scanf("%d", &E);

                Graph* graph = createGraph(V);
                printf("Enter Edges as: Source Destination Weight\n");
                for (int i = 0; i < E; i++) {
                    int u, v, w;
                    scanf("%d %d %d", &u, &v, &w);
                    addEdge(graph, u, v, w);
                }

                int src;
                printf("Enter Source Intersection: ");
                scanf("%d", &src);

                printf("\nCalculating Shortest Paths from Source %d...\n", src);
                dijkstra(graph, src, 1);
                
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
