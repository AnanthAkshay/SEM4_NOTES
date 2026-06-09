#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high)
{
    int pivot = arr[high];

    int i = low - 1;

    for(int j = low; j < high; j++)
    {
        if(arr[j] <= pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[high]);

    return i + 1;
}

int randomPartition(int arr[], int low, int high)
{
    int randomPivot =
        low + rand() % (high - low + 1);

    swap(&arr[randomPivot], &arr[high]);

    return partition(arr, low, high);
}

void quickSort(int arr[], int low, int high)
{
    if(low < high)
    {
        int pi =
            randomPartition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main()
{
    int n = 1000;

    int arr[n];

    srand(time(NULL));

    for(int i = 0; i < n; i++)
        arr[i] = rand() % 10000;

    clock_t start = clock();

    quickSort(arr, 0, n - 1);

    clock_t end = clock();

    double executionTime =
        (double)(end - start) / CLOCKS_PER_SEC;

    printf("First 20 Sorted Package IDs:\n");

    for(int i = 0; i < 20; i++)
        printf("%d ", arr[i]);

    printf("\n");

    printf("Execution Time = %lf seconds\n",
            executionTime);

    return 0;
}
