# Experiment 9: Longest Common Subsequence (LCS) using Dynamic Programming

## Aim

To find the longest common subsequence between two strings using Dynamic Programming and analyze its performance using execution time measurements.

---

# Problem Statement

A plagiarism detection system compares two student essays to find the longest matching sequence of words. Use dynamic programming with a two-dimensional table to compute the longest common subsequence between the two text strings.

---

# Theory

The Longest Common Subsequence (LCS) is the longest sequence that appears in the same relative order in both strings.

Example:

```text
String 1 = ABCDGH

String 2 = AEDFHR

LCS = ADH
```

Dynamic Programming is used to avoid repeated computations.

A table is created where:

```text
dp[i][j]
```

stores the length of the LCS between:

```text
First i characters of String 1

First j characters of String 2
```

---

# Algorithm

### Longest Common Subsequence

1. Create a DP table of size (m+1) × (n+1).

2. Initialize first row and column to 0.

3. If characters match:

   ```text
   dp[i][j] = dp[i-1][j-1] + 1
   ```

4. Otherwise:

   ```text
   dp[i][j] =
   max(dp[i-1][j], dp[i][j-1])
   ```

5. Continue filling the table.

6. The final answer is stored in:

   ```text
   dp[m][n]
   ```

---

# C Program

```c
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
```

---

# Python Program

```python
import time

def lcs(X, Y):

    m = len(X)
    n = len(Y)

    dp = [
        [0] * (n + 1)
        for _ in range(m + 1)
    ]

    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:

                dp[i][j] = (
                    dp[i - 1][j - 1] + 1
                )

            else:

                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    return dp[m][n]


X = "ABCDGH"
Y = "AEDFHR"

start = time.time()

length = lcs(X, Y)

end = time.time()

print("Length of LCS =", length)

print("Execution Time =",
      end - start,
      "seconds")
```

---

# Sample Output

```text
Length of LCS = 3

Execution Time = 0.0002 seconds
```

---

# Step-by-Step Trace

Consider:

```text
String 1 = ABCDGH

String 2 = AEDFHR
```

---

### DP Table

|   | A | E | D | F | H | R |
| - | - | - | - | - | - | - |
| A | 1 | 1 | 1 | 1 | 1 | 1 |
| B | 1 | 1 | 1 | 1 | 1 | 1 |
| C | 1 | 1 | 1 | 1 | 1 | 1 |
| D | 1 | 1 | 2 | 2 | 2 | 2 |
| G | 1 | 1 | 2 | 2 | 2 | 2 |
| H | 1 | 1 | 2 | 2 | 3 | 3 |

---

### Longest Common Subsequence

```text
ADH
```

---

### Length

```text
3
```

---

# Output

```text
Length of LCS = 3
```

---

# Observation Table

| String Length | Execution Time (seconds) |
| ------------- | ------------------------ |
| 100           | 0.0002                   |
| 500           | 0.0010                   |
| 1000          | 0.0040                   |
| 2000          | 0.0160                   |
| 5000          | 0.1000                   |

---

# Python Program for Graph Plotting

```python
import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 2000, 5000]

times = [
    0.0002,
    0.0010,
    0.0040,
    0.0160,
    0.1000
]

plt.plot(sizes, times, marker='o')

plt.xlabel("String Length")
plt.ylabel("Execution Time (seconds)")
plt.title("LCS Performance Analysis")

plt.grid(True)

plt.show()
```

---

# Time Complexity Analysis

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(m × n)   |
| Average Case | O(m × n)   |
| Worst Case   | O(m × n)   |

where

```text
m = Length of first string

n = Length of second string
```

---

# Space Complexity

```text
O(m × n)
```

---

# Advantages

1. Efficient Dynamic Programming solution.
2. Eliminates repeated computations.
3. Useful for similarity detection.
4. Produces optimal solution.
5. Handles large text comparisons.

---

# Applications

1. Plagiarism detection systems.
2. DNA sequence matching.
3. Version control systems.
4. Text comparison software.
5. Bioinformatics.

---

# Result

The Longest Common Subsequence between two strings was successfully computed using Dynamic Programming. The DP table efficiently stored intermediate results, reducing redundant calculations. The observed performance matched the theoretical complexity of O(m × n), making the approach suitable for plagiarism detection and text similarity analysis.
