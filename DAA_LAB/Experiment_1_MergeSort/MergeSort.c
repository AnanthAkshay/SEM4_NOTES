#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to merge two halves
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // Create temporary arrays
    int *L = (int *)malloc(n1 * sizeof(int));
    int *R = (int *)malloc(n2 * sizeof(int));

    // Copy data to temporary arrays L[] and R[]
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    // Merge the temporary arrays back into arr[left..right]
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) { // Stable sort condition (<=)
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of L[], if there are any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy the remaining elements of R[], if there are any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }

    // Free allocated memory
    free(L);
    free(R);
}

// Function to sort an array using Merge Sort
void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        // Sort first and second halves
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // Merge the sorted halves
        merge(arr, left, mid, right);
    }
}

// Function to print an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// Function to perform performance analysis
void performanceAnalysis() {
    int sizes[] = {1, 10, 100, 1000, 10000, 100000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    printf("\n--- Performance Analysis ---\n");
    printf("%-10s | %-20s\n", "N", "Time Taken (seconds)");
    printf("------------------------------------\n");

    for (int i = 0; i < num_sizes; i++) {
        int n = sizes[i];
        int *arr = (int *)malloc(n * sizeof(int));
        
        // Fill array with random values (representing random customer orders)
        for (int j = 0; j < n; j++) {
            arr[j] = rand() % 1000000;
        }

        clock_t start = clock();
        mergeSort(arr, 0, n - 1);
        clock_t end = clock();

        double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("%-10d | %-20f\n", n, time_taken);

        free(arr);
    }
    printf("------------------------------------\n");
}

// Main function (Menu Driven)
int main() {
    int choice;
    srand(time(0));

    while (1) {
        printf("\n==================================\n");
        printf("    ONLINE RETAIL ORDER SORTING   \n");
        printf("==================================\n");
        printf("1. Sort Custom Array (Manual Input)\n");
        printf("2. Run Performance Analysis\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        if (scanf("%d", &choice) != 1) break;

        switch (choice) {
            case 1: {
                int n;
                printf("Enter number of orders: ");
                scanf("%d", &n);
                if(n <= 0) {
                    printf("Invalid size!\n");
                    break;
                }
                int *arr = (int *)malloc(n * sizeof(int));
                printf("Enter the order amounts: \n");
                for (int i = 0; i < n; i++) {
                    scanf("%d", &arr[i]);
                }
                printf("\nUnsorted Orders:\n");
                printArray(arr, n);

                mergeSort(arr, 0, n - 1);

                printf("\nSorted Orders:\n");
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
