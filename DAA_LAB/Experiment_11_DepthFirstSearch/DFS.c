#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 100

int graph[MAX][MAX];
int visited[MAX];

int discovery[MAX];
int finish[MAX];

int timer = 0;

void DFS(int node, int n)
{
    visited[node] = 1;

    discovery[node] = ++timer;

    for(int i = 0; i < n; i++)
    {
        if(graph[node][i] && !visited[i])
        {
            DFS(i, n);
        }
    }

    finish[node] = ++timer;
}

int main()
{
    int n = 10;

    srand(time(NULL));

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            graph[i][j] = rand() % 2;
        }
    }

    clock_t start = clock();

    DFS(0, n);

    clock_t end = clock();

    printf("Node\tDiscovery\tFinish\n");

    for(int i = 0; i < n; i++)
    {
        printf("%d\t%d\t\t%d\n",
               i,
               discovery[i],
               finish[i]);
    }

    double executionTime =
        (double)(end - start)
        / CLOCKS_PER_SEC;

    printf("\nExecution Time = %lf seconds\n",
           executionTime);

    return 0;
}
