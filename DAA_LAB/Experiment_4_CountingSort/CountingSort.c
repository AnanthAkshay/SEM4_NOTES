#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void countingSort(int arr[], int n)
{
    int count[101] = {0};
    int output[n];

    for(int i = 0; i < n; i++)
        count[arr[i]]++;

    for(int i = 1; i <= 100; i++)
        count[i] += count[i - 1];

    for(int i = n - 1; i >= 0; i--)
    {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }

    for(int i = 0; i < n; i++)
        arr[i] = output[i];
}

int main()
{
    int n = 1000;

    int marks[n];

    srand(time(NULL));

    for(int i = 0; i < n; i++)
        marks[i] = rand() % 101;

    clock_t start = clock();

    countingSort(marks, n);

    clock_t end = clock();

    double executionTime =
        (double)(end - start) /
        CLOCKS_PER_SEC;

    printf("First 20 Sorted Marks:\n");

    for(int i = 0; i < 20; i++)
        printf("%d ", marks[i]);

    printf("\n");

    printf("Execution Time = %lf seconds\n",
            executionTime);

    return 0;
}
