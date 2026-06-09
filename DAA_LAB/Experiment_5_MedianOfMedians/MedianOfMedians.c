#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int compare(const void *a, const void *b)
{
    return (*(int*)a - *(int*)b);
}

int median(int arr[], int n)
{
    qsort(arr, n, sizeof(int), compare);

    if(n % 2 == 0)
        return (arr[n/2 - 1] + arr[n/2]) / 2;

    return arr[n/2];
}

int main()
{
    int n = 1001;

    int waitingTime[n];

    srand(time(NULL));

    for(int i = 0; i < n; i++)
        waitingTime[i] = rand() % 500;

    clock_t start = clock();

    int med = median(waitingTime, n);

    clock_t end = clock();

    double executionTime =
        (double)(end - start) /
        CLOCKS_PER_SEC;

    printf("Median Waiting Time = %d minutes\n",
            med);

    printf("Execution Time = %lf seconds\n",
            executionTime);

    return 0;
}
