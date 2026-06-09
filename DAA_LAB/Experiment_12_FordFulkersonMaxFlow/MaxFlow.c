#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define MAX 10
#define INF 1000000000

int cap[MAX][MAX];
int parent[MAX];
int visited[MAX];
int q[MAX*MAX];

int bfs(int s, int t, int n)
{
    memset(visited, 0, sizeof(visited));

    int front = 0;
    int rear = 0;

    q[rear++] = s;

    visited[s] = 1;

    parent[s] = -1;

    while(front < rear)
    {
        int u = q[front++];

        for(int v = 0; v < n; v++)
        {
            if(!visited[v] &&
               cap[u][v] > 0)
            {
                visited[v] = 1;

                parent[v] = u;

                if(v == t)
                    return 1;

                q[rear++] = v;
            }
        }
    }

    return 0;
}

int maxFlow(int s, int t, int n)
{
    int total = 0;

    while(bfs(s, t, n))
    {
        int flow = INF;

        for(int v = t; v != s; v = parent[v])
        {
            if(cap[parent[v]][v] < flow)

                flow =
                cap[parent[v]][v];
        }

        for(int v = t; v != s; v = parent[v])
        {
            cap[parent[v]][v] -= flow;

            cap[v][parent[v]] += flow;
        }

        total += flow;
    }

    return total;
}

int main()
{
    int n = 6;

    memset(cap, 0, sizeof(cap));

    cap[0][1] = 16;
    cap[0][2] = 13;
    cap[1][2] = 10;
    cap[1][3] = 12;
    cap[2][4] = 14;
    cap[3][2] = 9;
    cap[3][5] = 20;
    cap[4][3] = 7;
    cap[4][5] = 4;

    clock_t start = clock();

    int result =
        maxFlow(0, 5, n);

    clock_t end = clock();

    double executionTime =
        (double)(end - start)
        / CLOCKS_PER_SEC;

    printf("Maximum Water Flow = %d units\n",
           result);

    printf("Execution Time = %lf seconds\n",
           executionTime);

    return 0;
}
