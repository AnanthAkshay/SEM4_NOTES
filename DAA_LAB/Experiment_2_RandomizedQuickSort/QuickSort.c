#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to swap two integers
void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

// Standard Lomuto partition scheme
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // Pivot is the last element
    int i = (low - 1); // Index of smaller element

    for (int j = low; j <= high - 1; j++) {
        // If current element is smaller than or equal to pivot
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

// Randomized partition
int randomizedPartition(int arr[], int low, int high) {
    // Generate a random index between low and high
    int random_idx = low + rand() % (high - low + 1);
    
    // Swap the randomly selected element with the last element
    swap(&arr[random_idx], &arr[high]);
    
    return partition(arr, low, high);
}

// Randomized Quick Sort
void randomizedQuickSort(int arr[], int low, int high) {
    if (low < high) {
        // Find pivot such that elements smaller are on left, greater on right
        int pi = randomizedPartition(arr, low, high);

        // Recursively sort elements before and after partition
        randomizedQuickSort(arr, low, pi - 1);
        randomizedQuickSort(arr, pi + 1, high);
    }
}

// Function to print an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// Performance Analysis Function
void performanceAnalysis() {
    int sizes[] = {1, 10, 100, 1000, 10000, 100000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    printf("\n--- Performance Analysis ---\n");
    printf("%-10s | %-20s\n", "N", "Time Taken (seconds)");
    printf("------------------------------------\n");

    for (int i = 0; i < num_sizes; i++) {
        int n = sizes[i];
        int *arr = (int *)malloc(n * sizeof(int));
        
        for (int j = 0; j < n; j++) {
            arr[j] = rand() % 1000000;
        }

        clock_t start = clock();
        randomizedQuickSort(arr, 0, n - 1);
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
        printf("\n=====================================\n");
        printf("  COURIER PACKAGE SORTING (R-QUICK)  \n");
        printf("=====================================\n");
        printf("1. Sort Custom Array (Manual Input)\n");
        printf("2. Run Performance Analysis\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        if (scanf("%d", &choice) != 1) break;

        switch (choice) {
            case 1: {
                int n;
                printf("Enter number of packages: ");
                scanf("%d", &n);
                if(n <= 0) {
                    printf("Invalid size!\n");
                    break;
                }
                int *arr = (int *)malloc(n * sizeof(int));
                printf("Enter the package weights/IDs: \n");
                for (int i = 0; i < n; i++) {
                    scanf("%d", &arr[i]);
                }
                printf("\nUnsorted Packages:\n");
                printArray(arr, n);

                randomizedQuickSort(arr, 0, n - 1);

                printf("\nSorted Packages:\n");
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
