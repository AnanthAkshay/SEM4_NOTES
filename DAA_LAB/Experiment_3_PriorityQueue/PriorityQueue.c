#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 10000

int heap[MAX];
int size = 0;

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void insert(int value)
{
    int i = size;

    heap[size++] = value;

    while(i > 0)
    {
        int parent = (i - 1) / 2;

        if(heap[parent] < heap[i])
        {
            swap(&heap[parent], &heap[i]);
            i = parent;
        }
        else
            break;
    }
}

void heapify(int i)
{
    int largest = i;

    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if(left < size &&
       heap[left] > heap[largest])
        largest = left;

    if(right < size &&
       heap[right] > heap[largest])
        largest = right;

    if(largest != i)
    {
        swap(&heap[i], &heap[largest]);
        heapify(largest);
    }
}

int extractMax()
{
    int root = heap[0];

    heap[0] = heap[size - 1];

    size--;

    heapify(0);

    return root;
}

int main()
{
    srand(time(NULL));

    int n = 1000;

    clock_t start = clock();

    for(int i = 0; i < n; i++)
    {
        int priority = rand() % 1000;

        insert(priority);
    }

    printf("Top 20 Boarding Priorities:\n");

    for(int i = 0; i < 20; i++)
        printf("%d ", extractMax());

    clock_t end = clock();

    double executionTime =
        (double)(end - start) /
        CLOCKS_PER_SEC;

    printf("\n");

    printf("Execution Time = %lf seconds\n",
            executionTime);

    return 0;
}
