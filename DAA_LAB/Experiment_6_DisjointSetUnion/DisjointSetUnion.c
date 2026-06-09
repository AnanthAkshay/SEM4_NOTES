#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 10000

int parent[MAX];
int rankArr[MAX];

void makeSet(int n)
{
    for(int i = 0; i < n; i++)
    {
        parent[i] = i;
        rankArr[i] = 0;
    }
}

int find(int x)
{
    if(parent[x] != x)
        parent[x] = find(parent[x]);

    return parent[x];
}

void unionSets(int x, int y)
{
    int rootX = find(x);
    int rootY = find(y);

    if(rootX == rootY)
        return;

    if(rankArr[rootX] < rankArr[rootY])
        parent[rootX] = rootY;

    else if(rankArr[rootX] > rankArr[rootY])
        parent[rootY] = rootX;

    else
    {
        parent[rootY] = rootX;
        rankArr[rootX]++;
    }
}

int main()
{
    int n = 1000;

    srand(time(NULL));

    makeSet(n);

    clock_t start = clock();

    for(int i = 0; i < 500; i++)
    {
        int a = rand() % n;
        int b = rand() % n;

        unionSets(a, b);
    }

    clock_t end = clock();

    double executionTime =
        (double)(end - start) /
        CLOCKS_PER_SEC;

    printf("Friend Groups:\n");

    for(int i = 0; i < 10; i++)
        printf("User %d -> Group %d\n",
               i,
               find(i));

    printf("\nExecution Time = %lf seconds\n",
           executionTime);

    return 0;
}
