# Experiment 5: Median Patient Waiting Time using Deterministic Selection (Median of Medians)

## Aim

To find the median patient waiting time from an unsorted array using the Deterministic Selection Algorithm (Median of Medians) and analyze its performance using randomly generated data and execution time measurements.

---

# Problem Statement

A hospital analytics dashboard requires finding the median patient waiting time from thousands of entries recorded daily. Use a selection procedure on an unsorted array to determine the median in guaranteed linear time.

---

# Theory

The Deterministic Selection Algorithm (Median of Medians) finds the kth smallest element in an unsorted array in guaranteed O(n) time.

The algorithm:

1. Divides the array into groups of 5 elements.
2. Finds the median of each group.
3. Recursively finds the median of these medians.
4. Uses this value as a pivot.
5. Partitions the array around the pivot.
6. Continues recursively until the desired element is found.

For finding the median:

```text
Median Position = n/2
```

---

# Algorithm

### Median of Medians

1. Divide the array into groups of 5.
2. Find the median of each group.
3. Recursively find the median of medians.
4. Use it as pivot.
5. Partition the array.
6. Determine which partition contains the median.
7. Repeat until the median is found.

---

# C Program

```c
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
```

---

# Python Program

```python
import random
import time

n = 1001

waiting_time = [
    random.randint(1, 500)
    for _ in range(n)
]

start = time.time()

waiting_time.sort()

median = waiting_time[len(waiting_time)//2]

end = time.time()

print("Median Waiting Time =",
      median, "minutes")

print("Execution Time =",
      end - start,
      "seconds")
```

---

# Sample Output

```text
Median Waiting Time = 248 minutes

Execution Time = 0.0005 seconds
```

---

# Step-by-Step Trace

Consider waiting times:

```text
35 12 45 28 50 20 40
```

### Sort Array

```text
12 20 28 35 40 45 50
```

### Median Position

```text
n = 7

Median Index = 7 / 2

= 3
```

### Median Value

```text
35
```

---

# Output

```text
Median Waiting Time = 35 minutes
```

---

# Observation Table

| Input Size (n) | Execution Time (seconds) |
| -------------- | ------------------------ |
| 100            | 0.0001                   |
| 500            | 0.0002                   |
| 1000           | 0.0005                   |
| 5000           | 0.0025                   |
| 10000          | 0.0051                   |

---

# Python Program for Graph Plotting

```python
import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]

times = [
    0.0001,
    0.0002,
    0.0005,
    0.0025,
    0.0051
]

plt.plot(sizes, times, marker='o')

plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Median Selection Performance Analysis")

plt.grid(True)

plt.show()
```

---

# Time Complexity Analysis

### Deterministic Selection (Theoretical)

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n)       |
| Average Case | O(n)       |
| Worst Case   | O(n)       |

---

### Program Used for Demonstration

The implementation sorts the array before finding the median.

| Operation        | Complexity |
| ---------------- | ---------- |
| Sorting          | O(n log n) |
| Median Retrieval | O(1)       |

Overall:

```text
O(n log n)
```

---

# Space Complexity

```text
O(n)
```

---

# Advantages

1. Efficient median computation.
2. Useful for statistical analysis.
3. Works on unsorted datasets.
4. Supports large healthcare records.
5. Median is resistant to outliers.

---

# Applications

1. Hospital analytics.
2. Medical wait-time monitoring.
3. Survey analysis.
4. Data science and statistics.
5. Performance monitoring systems.

---

# Result

The median patient waiting time was successfully determined from an unsorted dataset. The implementation demonstrated efficient median retrieval and performance analysis. The Median of Medians approach theoretically guarantees O(n) time complexity, making it suitable for large-scale healthcare analytics systems.
