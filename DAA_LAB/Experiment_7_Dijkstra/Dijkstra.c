#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

#define V 100

int graph[V][V];

int minDistance(int dist[], int visited[], int n)
{
    int min = INT_MAX;
    int minIndex = -1;

    for(int i = 0; i < n; i++)
    {
        if(!visited[i] && dist[i] < min)
        {
            min = dist[i];
            minIndex = i;
        }
    }

    return minIndex;
}

void dijkstra(int n, int source)
{
    int dist[V];
    int visited[V];

    for(int i = 0; i < n; i++)
    {
        dist[i] = INT_MAX;
        visited[i] = 0;
    }

    dist[source] = 0;

    for(int count = 0; count < n - 1; count++)
    {
        int u =
            minDistance(dist, visited, n);

        visited[u] = 1;

        for(int v = 0; v < n; v++)
        {
            if(!visited[v] &&
               graph[u][v] &&
               dist[u] != INT_MAX &&
               dist[u] + graph[u][v] < dist[v])
            {
                dist[v] =
                    dist[u] + graph[u][v];
            }
        }
    }

    printf("Shortest Distances:\n");

    for(int i = 0; i < 10; i++)
        printf("Node %d : %d\n",
                i,
                dist[i]);
}

int main()
{
    int n = 100;

    srand(time(NULL));

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(i == j)
                graph[i][j] = 0;
            else
                graph[i][j] =
                    rand() % 20 + 1;
        }
    }

    clock_t start = clock();

    dijkstra(n, 0);

    clock_t end = clock();

    double executionTime =
        (double)(end - start) /
        CLOCKS_PER_SEC;

    printf("\nExecution Time = %lf seconds\n",
            executionTime);

    return 0;
}
