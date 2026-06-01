#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Returns maximum of two integers
int max(int a, int b) {
    return (a > b) ? a : b;
}

// Function to find length of LCS and print it
int lcs(char *X, char *Y, int m, int n, int verbose) {
    int **L = (int **)malloc((m + 1) * sizeof(int *));
    for (int i = 0; i <= m; i++)
        L[i] = (int *)malloc((n + 1) * sizeof(int));

    // Build the L[m+1][n+1] table in bottom-up fashion
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0)
                L[i][j] = 0;
            else if (X[i - 1] == Y[j - 1])
                L[i][j] = L[i - 1][j - 1] + 1;
            else
                L[i][j] = max(L[i - 1][j], L[i][j - 1]);
        }
    }

    int length = L[m][n];

    if (verbose) {
        // Code to print the LCS
        int index = length;
        char *lcs_str = (char *)malloc((index + 1) * sizeof(char));
        lcs_str[index] = '\0'; // Set the terminating character

        // Start from the bottom right corner and traverse
        int i = m, j = n;
        while (i > 0 && j > 0) {
            if (X[i - 1] == Y[j - 1]) {
                lcs_str[index - 1] = X[i - 1]; // Put current character in result
                i--; j--; index--;     // Reduce values of i, j and index
            }
            else if (L[i - 1][j] > L[i][j - 1])
                i--;
            else
                j--;
        }

        printf("Longest Matching Sequence: \"%s\"\n", lcs_str);
        printf("Length of LCS: %d\n", length);
        free(lcs_str);
    }

    // Free memory
    for (int i = 0; i <= m; i++)
        free(L[i]);
    free(L);

    return length;
}

// Helper to generate random DNA-like strings for testing
void generateRandomString(char *str, int length) {
    char charset[] = "ACTG";
    for (int i = 0; i < length; i++) {
        int key = rand() % (int)(sizeof(charset) - 1);
        str[i] = charset[key];
    }
    str[length] = '\0';
}

void performanceAnalysis() {
    int sizes[] = {10, 100, 500, 1000, 2000, 5000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    printf("\n--- Performance Analysis (LCS DP: O(M*N)) ---\n");
    printf("%-20s | %-20s\n", "String Lengths (N)", "Time Taken (seconds)");
    printf("---------------------------------------------\n");

    for (int i = 0; i < num_sizes; i++) {
        int n = sizes[i];
        char *X = (char *)malloc((n + 1) * sizeof(char));
        char *Y = (char *)malloc((n + 1) * sizeof(char));

        generateRandomString(X, n);
        generateRandomString(Y, n);

        clock_t start = clock();
        lcs(X, Y, n, n, 0); // verbose = 0
        clock_t end = clock();

        double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("%-20d | %-20f\n", n, time_taken);

        free(X);
        free(Y);
    }
    printf("---------------------------------------------\n");
}

int main() {
    int choice;
    srand(time(0));

    while (1) {
        printf("\n=========================================\n");
        printf(" PLAGIARISM DETECTION SYSTEM (LCS DP)    \n");
        printf("=========================================\n");
        printf("1. Compare Two Strings (Detect Plagiarism)\n");
        printf("2. Run Performance Analysis\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        if (scanf("%d", &choice) != 1) break;

        switch (choice) {
            case 1: {
                char X[1000], Y[1000];
                printf("Enter first string (Essay 1): ");
                scanf("%s", X);
                printf("Enter second string (Essay 2): ");
                scanf("%s", Y);

                int m = strlen(X);
                int n = strlen(Y);

                printf("\nAnalyzing...\n");
                lcs(X, Y, m, n, 1);
                
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
