#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Structure to represent a Disjoint Set
typedef struct {
    int *parent;
    int *rank;
    int n;
} DSU;

// Function to create and initialize the DSU
DSU* createDSU(int n) {
    DSU *dsu = (DSU *)malloc(sizeof(DSU));
    dsu->n = n;
    dsu->parent = (int *)malloc(n * sizeof(int));
    dsu->rank = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        dsu->parent[i] = i; // Every node is a parent of itself initially
        dsu->rank[i] = 0;   // Rank is initially 0
    }
    return dsu;
}

// Find operation with Path Compression
int find(DSU *dsu, int i) {
    if (dsu->parent[i] != i) {
        // Path compression: directly link the node to the root
        dsu->parent[i] = find(dsu, dsu->parent[i]);
    }
    return dsu->parent[i];
}

// Union operation with Union by Rank
void unionSet(DSU *dsu, int x, int y) {
    int rootX = find(dsu, x);
    int rootY = find(dsu, y);

    // If they are already in the same set, do nothing
    if (rootX == rootY) return;

    // Union by Rank: attach smaller rank tree under root of higher rank tree
    if (dsu->rank[rootX] < dsu->rank[rootY]) {
        dsu->parent[rootX] = rootY;
    } else if (dsu->rank[rootX] > dsu->rank[rootY]) {
        dsu->parent[rootY] = rootX;
    } else {
        // If ranks are same, make one as root and increment its rank
        dsu->parent[rootY] = rootX;
        dsu->rank[rootX]++;
    }
}

// Function to check if two users are friends (in the same set)
int areFriends(DSU *dsu, int x, int y) {
    return find(dsu, x) == find(dsu, y);
}

// Free DSU memory
void freeDSU(DSU *dsu) {
    free(dsu->parent);
    free(dsu->rank);
    free(dsu);
}

// Performance Analysis Function
void performanceAnalysis() {
    int sizes[] = {1, 10, 100, 1000, 10000, 100000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    printf("\n--- Performance Analysis (DSU: N Union ops) ---\n");
    printf("%-10s | %-20s\n", "N", "Time Taken (seconds)");
    printf("------------------------------------\n");

    for (int i = 0; i < num_sizes; i++) {
        int n = sizes[i];
        DSU *dsu = createDSU(n);
        
        clock_t start = clock();
        // Perform N random Union operations
        for (int j = 0; j < n; j++) {
            int u = rand() % n;
            int v = rand() % n;
            unionSet(dsu, u, v);
        }
        clock_t end = clock();

        double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("%-10d | %-20f\n", n, time_taken);
        
        freeDSU(dsu);
    }
    printf("------------------------------------\n");
}

int main() {
    int choice, n = 0;
    DSU *dsu = NULL;
    srand(time(0));

    while (1) {
        printf("\n====================================\n");
        printf(" SOCIAL NETWORK FRIEND GROUPS (DSU) \n");
        printf("====================================\n");
        printf("1. Initialize Network (N users)\n");
        printf("2. Make Friends (Union)\n");
        printf("3. Check Friendship (Find)\n");
        printf("4. Run Performance Analysis\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        if (scanf("%d", &choice) != 1) break;

        switch (choice) {
            case 1:
                printf("Enter number of users in network: ");
                scanf("%d", &n);
                if (n <= 0) {
                    printf("Invalid number of users!\n");
                    break;
                }
                if (dsu) freeDSU(dsu);
                dsu = createDSU(n);
                printf("Network of %d users created. User IDs: 0 to %d\n", n, n-1);
                break;
            case 2:
                if (!dsu) { printf("Initialize network first!\n"); break; }
                int u, v;
                printf("Enter two User IDs to connect (e.g., 2 4): ");
                scanf("%d %d", &u, &v);
                if (u >= 0 && u < n && v >= 0 && v < n) {
                    unionSet(dsu, u, v);
                    printf("User %d and User %d are now in the same friend group!\n", u, v);
                } else {
                    printf("Invalid User IDs!\n");
                }
                break;
            case 3:
                if (!dsu) { printf("Initialize network first!\n"); break; }
                int x, y;
                printf("Enter two User IDs to check friendship: ");
                scanf("%d %d", &x, &y);
                if (x >= 0 && x < n && y >= 0 && y < n) {
                    if (areFriends(dsu, x, y))
                        printf("Yes! User %d and User %d belong to the same friend group.\n", x, y);
                    else
                        printf("No. User %d and User %d are in different groups.\n", x, y);
                } else {
                    printf("Invalid User IDs!\n");
                }
                break;
            case 4:
                performanceAnalysis();
                break;
            case 5:
                printf("Exiting program...\n");
                if (dsu) freeDSU(dsu);
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }
    return 0;
}
