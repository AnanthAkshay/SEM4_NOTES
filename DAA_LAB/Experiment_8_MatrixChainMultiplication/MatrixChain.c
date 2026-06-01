#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

// Print the optimal parenthesization
void printOptimalParens(int **s, int i, int j) {
    if (i == j) {
        printf("A%d", i);
    } else {
        printf("(");
        printOptimalParens(s, i, s[i][j]);
        printOptimalParens(s, s[i][j] + 1, j);
        printf(")");
    }
}

// Matrix Chain Multiplication using Dynamic Programming
int matrixChainOrder(int p[], int n, int verbose) {
    // For simplicity of indexing, matrices are 1..n
    // m[i][j] = Minimum number of scalar multiplications needed
    int **m = (int **)malloc((n + 1) * sizeof(int *));
    int **s = (int **)malloc((n + 1) * sizeof(int *));
    for (int i = 0; i <= n; i++) {
        m[i] = (int *)malloc((n + 1) * sizeof(int));
        s[i] = (int *)malloc((n + 1) * sizeof(int));
    }

    // cost is zero when multiplying one matrix
    for (int i = 1; i <= n; i++)
        m[i][i] = 0;

    // L is chain length
    for (int L = 2; L <= n; L++) {
        for (int i = 1; i <= n - L + 1; i++) {
            int j = i + L - 1;
            m[i][j] = INT_MAX;
            for (int k = i; k <= j - 1; k++) {
                // q = cost/scalar multiplications
                int q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j];
                if (q < m[i][j]) {
                    m[i][j] = q;
                    s[i][j] = k;
                }
            }
        }
    }

    int min_cost = m[1][n];

    if (verbose) {
        printf("\nOptimal Parenthesization: ");
        printOptimalParens(s, 1, n);
        printf("\nMinimum scalar multiplications: %d\n", min_cost);
    }

    // Free allocated memory
    for (int i = 0; i <= n; i++) {
        free(m[i]);
        free(s[i]);
    }
    free(m);
    free(s);

    return min_cost;
}

void performanceAnalysis() {
    int sizes[] = {10, 50, 100, 200, 500, 1000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    printf("\n--- Performance Analysis (Matrix Chain DP: O(N^3)) ---\n");
    printf("%-15s | %-20s\n", "Matrices (N)", "Time Taken (seconds)");
    printf("----------------------------------------\n");

    for (int i = 0; i < num_sizes; i++) {
        int n = sizes[i]; // Number of matrices
        // Array length is n + 1
        int *p = (int *)malloc((n + 1) * sizeof(int));
        
        for (int j = 0; j <= n; j++) {
            p[j] = (rand() % 100) + 1; // Random dimensions 1 to 100
        }

        clock_t start = clock();
        matrixChainOrder(p, n, 0); // verbose = 0
        clock_t end = clock();

        double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("%-15d | %-20f\n", n, time_taken);
        free(p);
    }
    printf("----------------------------------------\n");
}

int main() {
    int choice;
    srand(time(0));

    while (1) {
        printf("\n=========================================\n");
        printf(" VIDEO PROCESSING ENGINE (MCM DP)        \n");
        printf("=========================================\n");
        printf("1. Calculate Optimal Matrix Multiplication\n");
        printf("2. Run Performance Analysis\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        if (scanf("%d", &choice) != 1) break;

        switch (choice) {
            case 1: {
                int n;
                printf("Enter number of matrices: ");
                scanf("%d", &n);
                if (n <= 1) {
                    printf("Requires at least 2 matrices.\n");
                    break;
                }
                
                int *p = (int *)malloc((n + 1) * sizeof(int));
                printf("Enter the dimensions array (size %d): \n", n + 1);
                for (int i = 0; i <= n; i++) {
                    scanf("%d", &p[i]);
                }

                matrixChainOrder(p, n, 1);
                
                free(p);
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
