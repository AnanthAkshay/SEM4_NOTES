#include <stdio.h>
#include <string.h>
#include <time.h>

int max(int a, int b)
{
    return (a > b) ? a : b;
}

int lcs(char X[], char Y[])
{
    int m = strlen(X);
    int n = strlen(Y);

    int dp[m + 1][n + 1];

    for(int i = 0; i <= m; i++)
    {
        for(int j = 0; j <= n; j++)
        {
            if(i == 0 || j == 0)
                dp[i][j] = 0;

            else if(X[i - 1] == Y[j - 1])
                dp[i][j] =
                    dp[i - 1][j - 1] + 1;

            else
                dp[i][j] =
                    max(dp[i - 1][j],
                        dp[i][j - 1]);
        }
    }

    return dp[m][n];
}

int main()
{
    char X[] = "ABCDGH";
    char Y[] = "AEDFHR";

    clock_t start = clock();

    int length = lcs(X, Y);

    clock_t end = clock();

    double executionTime =
        (double)(end - start) /
        CLOCKS_PER_SEC;

    printf("Length of LCS = %d\n",
            length);

    printf("Execution Time = %lf seconds\n",
            executionTime);

    return 0;
}
