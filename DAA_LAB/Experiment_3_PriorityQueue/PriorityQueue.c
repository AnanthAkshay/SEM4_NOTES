#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_SIZE 1000000

// Priority Queue structure using a Max Heap
typedef struct {
    int size;
    int data[MAX_SIZE];
} MaxHeap;

// Function to swap two integers
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to initialize the heap
void initHeap(MaxHeap *h) {
    h->size = 0;
}

// Function to maintain the Max Heap property (Heapify Down)
void heapify(MaxHeap *h, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < h->size && h->data[left] > h->data[largest])
        largest = left;

    if (right < h->size && h->data[right] > h->data[largest])
        largest = right;

    if (largest != i) {
        swap(&h->data[i], &h->data[largest]);
        heapify(h, largest);
    }
}

// Function to insert a new element (Heapify Up)
void insert(MaxHeap *h, int val) {
    if (h->size >= MAX_SIZE) {
        printf("Priority Queue is full!\n");
        return;
    }

    int i = h->size;
    h->data[i] = val;
    h->size++;

    // Heapify Up
    while (i != 0 && h->data[(i - 1) / 2] < h->data[i]) {
        swap(&h->data[i], &h->data[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}

// Function to extract the maximum element (Extract Max)
int extractMax(MaxHeap *h) {
    if (h->size <= 0) {
        printf("Priority Queue is empty!\n");
        return -1;
    }
    if (h->size == 1) {
        h->size--;
        return h->data[0];
    }

    int root = h->data[0];
    h->data[0] = h->data[h->size - 1];
    h->size--;
    
    heapify(h, 0);

    return root;
}

// Function to get the maximum element without removing it (Peek)
int peek(MaxHeap *h) {
    if (h->size <= 0) {
        printf("Priority Queue is empty!\n");
        return -1;
    }
    return h->data[0];
}

// Function to print the heap
void printHeap(MaxHeap *h) {
    for (int i = 0; i < h->size; ++i)
        printf("%d ", h->data[i]);
    printf("\n");
}

// Performance Analysis Function
void performanceAnalysis() {
    int sizes[] = {1, 10, 100, 1000, 10000, 100000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    printf("\n--- Performance Analysis (Extract Max Time) ---\n");
    printf("%-10s | %-20s\n", "N", "Time Taken (seconds)");
    printf("------------------------------------\n");

    for (int i = 0; i < num_sizes; i++) {
        int n = sizes[i];
        MaxHeap h;
        initHeap(&h);
        
        // Insert N random elements
        for (int j = 0; j < n; j++) {
            insert(&h, rand() % 1000000);
        }

        // Measure time taken to extract max N times
        clock_t start = clock();
        for (int j = 0; j < n; j++) {
            extractMax(&h);
        }
        clock_t end = clock();

        double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("%-10d | %-20f\n", n, time_taken);
    }
    printf("------------------------------------\n");
}

int main() {
    int choice, val;
    MaxHeap h;
    initHeap(&h);
    srand(time(0));

    while (1) {
        printf("\n==================================\n");
        printf(" AIRLINE BOARDING PRIORITY SYSTEM \n");
        printf("==================================\n");
        printf("1. Insert Passenger (Priority Score)\n");
        printf("2. Extract Highest Priority (Board)\n");
        printf("3. Peek Highest Priority\n");
        printf("4. Display All Waiting Passengers\n");
        printf("5. Run Performance Analysis\n");
        printf("6. Exit\n");
        printf("Enter your choice: ");
        if (scanf("%d", &choice) != 1) break;

        switch (choice) {
            case 1:
                printf("Enter Priority Score: ");
                scanf("%d", &val);
                insert(&h, val);
                printf("Passenger with score %d inserted.\n", val);
                break;
            case 2:
                val = extractMax(&h);
                if (val != -1)
                    printf("Boarding passenger with score: %d\n", val);
                break;
            case 3:
                val = peek(&h);
                if (val != -1)
                    printf("Next passenger to board has score: %d\n", val);
                break;
            case 4:
                printf("Waiting passengers (Heap Array): ");
                printHeap(&h);
                break;
            case 5:
                performanceAnalysis();
                break;
            case 6:
                printf("Exiting program...\n");
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }
    return 0;
}
