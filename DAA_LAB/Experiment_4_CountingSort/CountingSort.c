#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_MARK 100

// Function to perform Counting Sort on marks array (0 to 100)
void countingSort(int arr[], int n) {
    int count[MAX_MARK + 1] = {0};
    int *output = (int *)malloc(n * sizeof(int));

    // Store count of each mark
    for (int i = 0; i < n; i++) {
        if(arr[i] >= 0 && arr[i] <= MAX_MARK)
            count[arr[i]]++;
        else {
            printf("Error: Mark %d out of bounds (0-100)\n", arr[i]);
            free(output);
            return;
        }
    }

    // Change count[i] so that count[i] now contains actual
    // position of this mark in output array
    for (int i = 1; i <= MAX_MARK; i++) {
        count[i] += count[i - 1];
    }

    // Build the output array (backward to maintain stability if objects were attached)
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }

    // Copy the output array to arr, so that arr now contains sorted characters
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
    
    free(output);
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

void performanceAnalysis() {
    int sizes[] = {1, 10, 100, 1000, 10000, 100000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    printf("\n--- Performance Analysis (Counting Sort) ---\n");
    printf("%-10s | %-20s\n", "N", "Time Taken (seconds)");
    printf("------------------------------------\n");

    for (int i = 0; i < num_sizes; i++) {
        int n = sizes[i];
        int *arr = (int *)malloc(n * sizeof(int));
        
        for (int j = 0; j < n; j++) {
            arr[j] = rand() % (MAX_MARK + 1); // Random marks 0 to 100
        }

        clock_t start = clock();
        countingSort(arr, n);
        clock_t end = clock();

        double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("%-10d | %-20f\n", n, time_taken);
        free(arr);
    }
    printf("------------------------------------\n");
}

int main() {
    int choice;
    srand(time(0));

    while (1) {
        printf("\n==================================\n");
        printf(" EXAM EVALUATION (COUNTING SORT)  \n");
        printf("==================================\n");
        printf("1. Sort Custom Marks Array\n");
        printf("2. Run Performance Analysis\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        if (scanf("%d", &choice) != 1) break;

        switch (choice) {
            case 1: {
                int n;
                printf("Enter number of students: ");
                scanf("%d", &n);
                if(n <= 0) {
                    printf("Invalid size!\n");
                    break;
                }
                int *arr = (int *)malloc(n * sizeof(int));
                printf("Enter the marks (0 to 100): \n");
                for (int i = 0; i < n; i++) {
                    scanf("%d", &arr[i]);
                }
                printf("\nUnsorted Marks:\n");
                printArray(arr, n);

                countingSort(arr, n);

                printf("\nSorted Marks:\n");
                printArray(arr, n);
                free(arr);
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
