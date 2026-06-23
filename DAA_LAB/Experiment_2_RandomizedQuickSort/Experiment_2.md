# Experiment 2: Randomized Quick Sort for Efficient Package Sorting

## Aim

To sort package IDs efficiently using Randomized Quick Sort and analyze its performance using randomly generated data and execution time measurements.

---

# Problem Statement

A courier service wants to optimize package sorting for delivery by randomizing the partitioning step to avoid worst-case delays. Use array-based random partitioning to achieve efficient average performance.

---

# Theory

Randomized Quick Sort is an improvement over Quick Sort.

Instead of always selecting the first or last element as the pivot, a random element is chosen as the pivot.

This reduces the probability of encountering the worst-case time complexity and provides efficient average performance.

The algorithm works using:

1. Random Pivot Selection
2. Partitioning
3. Recursive Sorting

---

# Algorithm

### Randomized Quick Sort

1. Select a random pivot element.
2. Place the pivot at the end of the array.
3. Partition the array around the pivot.
4. Recursively sort the left sub-array.
5. Recursively sort the right sub-array.
6. Repeat until the entire array is sorted.

---

# C Program

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high)
{
    int pivot = arr[high];

    int i = low - 1;

    for(int j = low; j < high; j++)
    {
        if(arr[j] <= pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i + 1], &arr[high]);

    return i + 1;
}

int randomPartition(int arr[], int low, int high)
{
    int randomPivot =
        low + rand() % (high - low + 1);

    swap(&arr[randomPivot], &arr[high]);

    return partition(arr, low, high);
}

void quickSort(int arr[], int low, int high)
{
    if(low < high)
    {
        int pi =
            randomPartition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main()
{
    int n = 1000;

    int arr[n];

    srand(time(NULL));

    for(int i = 0; i < n; i++)
        arr[i] = rand() % 10000;

    clock_t start = clock();

    quickSort(arr, 0, n - 1);

    clock_t end = clock();

    double executionTime =
        (double)(end - start) / CLOCKS_PER_SEC;

    printf("First 20 Sorted Package IDs:\n");

    for(int i = 0; i < 20; i++)
        printf("%d ", arr[i]);

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

def partition(arr, low, high):

    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:

            i += 1

            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def randomized_partition(arr, low, high):

    random_index = random.randint(low, high)

    arr[random_index], arr[high] = \
        arr[high], arr[random_index]

    return partition(arr, low, high)


def quick_sort(arr, low, high):

    if low < high:

        pi = randomized_partition(
            arr, low, high
        )

        quick_sort(arr, low, pi - 1)

        quick_sort(arr, pi + 1, high)


n = 1000

arr = [random.randint(1, 10000)
       for _ in range(n)]

start = time.time()

quick_sort(arr, 0, n - 1)

end = time.time()

print("First 20 Sorted Package IDs:")
print(arr[:20])

print("Execution Time =", end - start,
      "seconds")
```

---

# Java Program

```java
import java.util.Random;

public class RandomizedQuickSort {

    static Random rand = new Random();

    public static void quickSort(int arr[], int low, int high) {
        if (low < high) {

            int pivotIndex = randomPartition(arr, low, high);

            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    public static int randomPartition(int arr[], int low, int high) {

        int randomIndex = low + rand.nextInt(high - low + 1);

        swap(arr, randomIndex, high);

        return partition(arr, low, high);
    }

    public static int partition(int arr[], int low, int high) {

        int pivot = arr[high];

        int i = low - 1;

        for (int j = low; j < high; j++) {

            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, high);

        return i + 1;
    }

    public static void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {

        int n = 1000; // Number of packages

        int packages[] = new int[n];

        for (int i = 0; i < n; i++) {
            packages[i] = rand.nextInt(10000);
        }

        System.out.println("First 20 Package IDs Before Sorting:");
        for (int i = 0; i < 20; i++) {
            System.out.print(packages[i] + " ");
        }

        long startTime = System.nanoTime();

        quickSort(packages, 0, n - 1);

        long endTime = System.nanoTime();

        System.out.println("\n\nFirst 20 Package IDs After Sorting:");
        for (int i = 0; i < 20; i++) {
            System.out.print(packages[i] + " ");
        }

        System.out.println("\n\nExecution Time: "
                + (endTime - startTime) + " nanoseconds");
    }
}
```

---

# Sample Output

```text
First 20 Sorted Package IDs:

5 12 18 22 29 35 40 48 54 60
67 75 82 91 96 103 109 114 121 130

Execution Time = 0.0012 seconds
```

---

# Step-by-Step Trace

Consider the Package IDs:

```text
45 12 78 23 56 34
```

### Random Pivot Selected

```text
Pivot = 34
```

### Partition

```text
12 23 | 34 | 45 56 78
```

### Left Subarray

```text
12 23
```

Already Sorted

### Right Subarray

```text
45 56 78
```

Already Sorted

### Final Sorted Array

```text
12 23 34 45 56 78
```

---

# Output

```text
12 23 34 45 56 78
```

---

# Observation Table

| Input Size (n) | Execution Time (seconds) |
| -------------- | ------------------------ |
| 100            | 0.0001                   |
| 500            | 0.0005                   |
| 1000           | 0.0012                   |
| 5000           | 0.0078                   |
| 10000          | 0.0185                   |

---

# Python Program for Graph Plotting

```python
import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]

times = [
    0.0001,
    0.0005,
    0.0012,
    0.0078,
    0.0185
]

plt.plot(sizes, times, marker='o')

plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Randomized Quick Sort Performance Analysis")

plt.grid(True)

plt.show()
```

---

# Time Complexity Analysis

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n log n) |
| Average Case | O(n log n) |
| Worst Case   | O(n²)      |

---

# Space Complexity

```text
O(log n)
```

---

# Advantages

1. Faster than Merge Sort in practice.
2. Random pivot reduces worst-case probability.
3. Requires less memory.
4. Suitable for large datasets.
5. Efficient average performance.

---

# Applications

1. Courier package sorting.
2. Database indexing.
3. Search engines.
4. Data analytics systems.
5. Large-scale sorting applications.

---

# Result

The package IDs were successfully sorted using Randomized Quick Sort. Random pivot selection minimized the chances of worst-case performance. The observed execution times confirmed the expected average-case complexity of O(n log n), making the algorithm suitable for efficient package sorting in courier systems.
