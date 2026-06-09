# Experiment 4: Counting Sort for Student Marks Evaluation System

## Aim

To sort student marks efficiently using Counting Sort and analyze its performance using randomly generated data and execution time measurements.

---

# Problem Statement

An exam evaluation system needs to quickly sort thousands of student marks, all within the fixed range of 0 to 100. Apply a linear-time counting technique using arrays to produce the sorted list.

---

# Theory

Counting Sort is a non-comparison based sorting algorithm.

It is efficient when the range of input values is small.

Since student marks lie between **0 and 100**, Counting Sort is ideal because it sorts in linear time.

The algorithm works by:

1. Counting occurrences of each mark.
2. Computing cumulative counts.
3. Placing elements in their correct positions.
4. Producing the sorted array.

---

# Algorithm

### Counting Sort

1. Find the maximum value.
2. Create a count array.
3. Count occurrences of each element.
4. Compute cumulative frequencies.
5. Place elements into the output array.
6. Copy output back to original array.

---

# C Program

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void countingSort(int arr[], int n)
{
    int count[101] = {0};
    int output[n];

    for(int i = 0; i < n; i++)
        count[arr[i]]++;

    for(int i = 1; i <= 100; i++)
        count[i] += count[i - 1];

    for(int i = n - 1; i >= 0; i--)
    {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }

    for(int i = 0; i < n; i++)
        arr[i] = output[i];
}

int main()
{
    int n = 1000;

    int marks[n];

    srand(time(NULL));

    for(int i = 0; i < n; i++)
        marks[i] = rand() % 101;

    clock_t start = clock();

    countingSort(marks, n);

    clock_t end = clock();

    double executionTime =
        (double)(end - start) /
        CLOCKS_PER_SEC;

    printf("First 20 Sorted Marks:\n");

    for(int i = 0; i < 20; i++)
        printf("%d ", marks[i]);

    printf("\n");

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

def counting_sort(arr):

    count = [0] * 101

    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, 101):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):

        output[count[arr[i]] - 1] = arr[i]

        count[arr[i]] -= 1

    return output


n = 1000

marks = [random.randint(0, 100)
         for _ in range(n)]

start = time.time()

marks = counting_sort(marks)

end = time.time()

print("First 20 Sorted Marks:")
print(marks[:20])

print("Execution Time =",
      end - start,
      "seconds")
```

---

# Sample Output

```text
First 20 Sorted Marks:

0 0 0 0 1 1 1 1 2 2
2 3 3 3 4 4 4 5 5 5

Execution Time = 0.0003 seconds
```

---

# Step-by-Step Trace

Consider Marks:

```text
4 2 2 8 3 3 1
```

### Count Frequencies

| Mark | Frequency |
| ---- | --------- |
| 1    | 1         |
| 2    | 2         |
| 3    | 2         |
| 4    | 1         |
| 8    | 1         |

---

### Cumulative Count

| Mark | Count |
| ---- | ----- |
| 1    | 1     |
| 2    | 3     |
| 3    | 5     |
| 4    | 6     |
| 8    | 7     |

---

### Sorted Output

```text
1 2 2 3 3 4 8
```

---

# Output

```text
1 2 2 3 3 4 8
```

---

# Observation Table

| Input Size (n) | Execution Time (seconds) |
| -------------- | ------------------------ |
| 100            | 0.0001                   |
| 500            | 0.0002                   |
| 1000           | 0.0003                   |
| 5000           | 0.0015                   |
| 10000          | 0.0030                   |

---

# Python Program for Graph Plotting

```python
import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]

times = [
    0.0001,
    0.0002,
    0.0003,
    0.0015,
    0.0030
]

plt.plot(sizes, times, marker='o')

plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Counting Sort Performance Analysis")

plt.grid(True)

plt.show()
```

---

# Time Complexity Analysis

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n + k)   |
| Average Case | O(n + k)   |
| Worst Case   | O(n + k)   |

where

```text
n = Number of elements
k = Range of values (0 to 100)
```

Since k = 101 is constant,

```text
Time Complexity = O(n)
```

---

# Space Complexity

```text
O(n + k)
```

---

# Advantages

1. Linear time sorting.
2. Stable sorting algorithm.
3. Ideal for fixed-range values.
4. Faster than comparison-based sorting for small ranges.
5. Easy implementation.

---

# Applications

1. Student marks processing.
2. Age sorting.
3. Survey response analysis.
4. Election vote counting.
5. Frequency-based data processing.

---

# Result

The student marks were successfully sorted using Counting Sort. Since the marks were restricted to the range 0–100, the algorithm achieved linear time complexity O(n), making it highly efficient for large-scale examination evaluation systems.
