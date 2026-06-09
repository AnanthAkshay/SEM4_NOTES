#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void merge(int arr[], int left, int mid, int right)
{
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int L[n1], R[n2];

    for(int i = 0; i < n1; i++)
        L[i] = arr[left + i];

    for(int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;

    while(i < n1 && j < n2)
    {
        if(L[i] <= R[j])
            arr[k++] = L[i++];
        else
            arr[k++] = R[j++];
    }

    while(i < n1)
        arr[k++] = L[i++];

    while(j < n2)
        arr[k++] = R[j++];
}

void mergeSort(int arr[], int left, int right)
{
    if(left < right)
    {
        int mid = (left + right) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        merge(arr, left, mid, right);
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

    mergeSort(arr, 0, n - 1);

    clock_t end = clock();

    double executionTime =
        (double)(end - start) / CLOCKS_PER_SEC;

    printf("First 20 Sorted Order IDs:\n");

    for(int i = 0; i < 20; i++)
        printf("%d ", arr[i]);

    printf("\n");

    printf("Execution Time = %lf seconds\n",
            executionTime);

    return 0;
}
