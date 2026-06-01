#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to swap two elements
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Standard insertion sort to sort groups of 5
void insertionSort(int arr[], int left, int right) {
    for (int i = left + 1; i <= right; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= left && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// Function to find the median of a small array
int findMedian(int arr[], int left, int n) {
    insertionSort(arr, left, left + n - 1);
    return arr[left + n / 2];
}

// Standard Lomuto partition using a specific pivot
int partition(int arr[], int left, int right, int x) {
    int i;
    for (i = left; i < right; i++)
        if (arr[i] == x)
            break;
    swap(&arr[i], &arr[right]);

    int pivot = arr[right];
    i = left;
    for (int j = left; j <= right - 1; j++) {
        if (arr[j] <= pivot) {
            swap(&arr[i], &arr[j]);
            i++;
        }
    }
    swap(&arr[i], &arr[right]);
    return i;
}

// Median of Medians algorithm to find kth smallest element
int kthSmallest(int arr[], int left, int right, int k) {
    // If k is smaller than number of elements in array
    if (k > 0 && k <= right - left + 1) {
        int n = right - left + 1; // Number of elements
        
        // Divide arr[] in groups of size 5, calculate median
        // of every group and store it in median[] array.
        int i, *median = (int *)malloc(((n + 4) / 5) * sizeof(int));
        for (i = 0; i < n / 5; i++)
            median[i] = findMedian(arr, left + i * 5, 5);
        if (i * 5 < n) // For last group with less than 5 elements
        {
            median[i] = findMedian(arr, left + i * 5, n % 5);
            i++;
        }

        // Find median of all medians using recursive call.
        int medOfMed = (i == 1) ? median[0] : kthSmallest(median, 0, i - 1, i / 2 + 1);
        free(median);

        // Partition the array around a random element and get position of pivot
        int pos = partition(arr, left, right, medOfMed);

        // If position is same as k
        if (pos - left == k - 1)
            return arr[pos];
        if (pos - left > k - 1) // If position is more, recur for left
            return kthSmallest(arr, left, pos - 1, k);
        // Else recur for right subarray
        return kthSmallest(arr, pos + 1, right, k - pos + left - 1);
    }
    return -1; // Out of bounds
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

void performanceAnalysis() {
    int sizes[] = {1, 10, 100, 1000, 10000, 100000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    printf("\n--- Performance Analysis (Median of Medians) ---\n");
    printf("%-10s | %-20s\n", "N", "Time Taken (seconds)");
    printf("------------------------------------\n");

    for (int i = 0; i < num_sizes; i++) {
        int n = sizes[i];
        int *arr = (int *)malloc(n * sizeof(int));
        
        for (int j = 0; j < n; j++) {
            arr[j] = rand() % 10000; // Random waiting times
        }

        int k = n / 2 + 1; // Looking for median

        clock_t start = clock();
        kthSmallest(arr, 0, n - 1, k);
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
        printf(" HOSPITAL ANALYTICS (MEDIAN FIND) \n");
        printf("==================================\n");
        printf("1. Find Median Waiting Time\n");
        printf("2. Run Performance Analysis\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        if (scanf("%d", &choice) != 1) break;

        switch (choice) {
            case 1: {
                int n;
                printf("Enter number of patients: ");
                scanf("%d", &n);
                if(n <= 0) {
                    printf("Invalid size!\n");
                    break;
                }
                int *arr = (int *)malloc(n * sizeof(int));
                printf("Enter the waiting times (minutes): \n");
                for (int i = 0; i < n; i++) {
                    scanf("%d", &arr[i]);
                }
                printf("\nWaiting times:\n");
                printArray(arr, n);

                // Median is the (N/2 + 1)th smallest element
                int median = kthSmallest(arr, 0, n - 1, n / 2 + 1);

                printf("\nMedian Waiting Time: %d minutes\n", median);
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
