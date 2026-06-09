#include <stdio.h>
#include <limits.h>
#include <time.h>

int matrixChainOrder(int p[], int n)
{
    int dp[n][n];

    for(int i = 1; i < n; i++)
        dp[i][i] = 0;

    for(int len = 2; len < n; len++)
    {
        for(int i = 1; i < n - len + 1; i++)
        {
            int j = i + len - 1;

            dp[i][j] = INT_MAX;

            for(int k = i; k < j; k++)
            {
                int cost =
                    dp[i][k] +
                    dp[k+1][j] +
                    p[i-1] * p[k] * p[j];

                if(cost < dp[i][j])
                    dp[i][j] = cost;
            }
        }
    }

    return dp[1][n-1];
}

int main()
{
    int p[] = {30, 35, 15, 5, 10, 20, 25};

    int n = sizeof(p)/sizeof(p[0]);

    clock_t start = clock();

    int result =
        matrixChainOrder(p, n);

    clock_t end = clock();

    double executionTime =
        (double)(end - start) /
        CLOCKS_PER_SEC;

    printf("Minimum Multiplications = %d\n",
            result);

    printf("Execution Time = %lf seconds\n",
            executionTime);

    return 0;
}
