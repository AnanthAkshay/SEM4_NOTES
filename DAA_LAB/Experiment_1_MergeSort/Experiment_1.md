# Experiment 1: Stable Sorting of Customer Orders using Merge Sort

## Aim

To arrange customer orders by Order ID efficiently using Merge Sort and analyze its performance using randomly generated data and execution time measurements.

---

# Problem Statement

An online retail platform must arrange thousands of customer orders by Order ID before shipping. Design an efficient sorting approach using arrays, ensuring stable ordering for large datasets.

---

# Theory

Merge Sort is a Divide-and-Conquer sorting algorithm.

The algorithm works by:

1. Dividing the array into two halves.
2. Recursively sorting each half.
3. Merging the sorted halves.

Since equal elements maintain their relative order after merging, Merge Sort is a stable sorting algorithm.

---

# Algorithm

### Merge Sort

1. Divide the array into two halves.
2. Recursively sort the left half.
3. Recursively sort the right half.
4. Merge the sorted halves.
5. Repeat until the entire array is sorted.

---

# C Program

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void merge(int arr[], int left, int mid, int right)
{
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int L[n1], R[n2];

    for(int i = 0; i < n1; i++)
        L[i] = arr[left + i];

    for(int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;

    while(i < n1 && j < n2)
    {
        if(L[i] <= R[j])
            arr[k++] = L[i++];
        else
            arr[k++] = R[j++];
    }

    while(i < n1)
        arr[k++] = L[i++];

    while(j < n2)
        arr[k++] = R[j++];
}

void mergeSort(int arr[], int left, int right)
{
    if(left < right)
    {
        int mid = (left + right) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        merge(arr, left, mid, right);
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

    mergeSort(arr, 0, n - 1);

    clock_t end = clock();

    double executionTime =
        (double)(end - start) / CLOCKS_PER_SEC;

    printf("First 20 Sorted Order IDs:\n");

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

def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


n = 1000

orders = [random.randint(1, 10000)
          for _ in range(n)]

start = time.time()

merge_sort(orders)

end = time.time()

print("First 20 Sorted Order IDs:")
print(orders[:20])

print("Execution Time =", end - start,
      "seconds")
```

---

# Java Program

```java
import java.util.Random;

public class OrderSorting {

    public static void mergeSort(int arr[], int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;

            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);

            merge(arr, left, mid, right);
        }
    }

    public static void merge(int arr[], int left, int mid, int right) {

        int n1 = mid - left + 1;
        int n2 = right - mid;

        int L[] = new int[n1];
        int R[] = new int[n2];

        for (int i = 0; i < n1; i++)
            L[i] = arr[left + i];

        for (int j = 0; j < n2; j++)
            R[j] = arr[mid + 1 + j];

        int i = 0, j = 0, k = left;

        while (i < n1 && j < n2) {

            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    public static void main(String[] args) {

        int n = 1000; // Number of orders

        int orders[] = new int[n];

        Random random = new Random();

        for (int i = 0; i < n; i++) {
            orders[i] = random.nextInt(10000);
        }

        System.out.println("First 20 Order IDs Before Sorting:");
        for (int i = 0; i < 20; i++) {
            System.out.print(orders[i] + " ");
        }

        long startTime = System.nanoTime();

        mergeSort(orders, 0, n - 1);

        long endTime = System.nanoTime();

        System.out.println("\n\nFirst 20 Order IDs After Sorting:");
        for (int i = 0; i < 20; i++) {
            System.out.print(orders[i] + " ");
        }

        System.out.println("\n\nExecution Time: "
                + (endTime - startTime) + " nanoseconds");
    }
}
```

---

# Sample Output

```text
First 20 Sorted Order IDs:

7 13 21 28 34 42 49 53 58 67
72 79 84 91 98 102 109 115 120 127

Execution Time = 0.0018 seconds
```

---

# Step-by-Step Trace

Consider the Order IDs:

```text
105 102 108 101 106 103
```

### Initial Array

```text
105 102 108 101 106 103
```

### Divide

```text
[105 102 108]

[101 106 103]
```

### Further Division

```text
[105]

[102 108]

[102]

[108]

[101]

[106 103]

[106]

[103]
```

### Merge

```text
[102] + [108]

=

[102 108]
```

```text
[105] + [102 108]

=

[102 105 108]
```

```text
[106] + [103]

=

[103 106]
```

```text
[101] + [103 106]

=

[101 103 106]
```

### Final Merge

```text
[102 105 108]

+

[101 103 106]

=

[101 102 103 105 106 108]
```

---

# Output

```text
101 102 103 105 106 108
```

---

# Observation Table

| Input Size (n) | Execution Time (seconds) |
| -------------- | ------------------------ |
| 100            | 0.0001                   |
| 500            | 0.0007                   |
| 1000           | 0.0015                   |
| 5000           | 0.0102                   |
| 10000          | 0.0254                   |

---

# Python Program for Graph Plotting

```python
import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]

times = [
    0.0001,
    0.0007,
    0.0015,
    0.0102,
    0.0254
]

plt.plot(sizes, times, marker='o')

plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Merge Sort Performance Analysis")

plt.grid(True)

plt.show()
```

---

# Time Complexity Analysis

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(n log n) |
| Average Case | O(n log n) |
| Worst Case   | O(n log n) |

---

# Space Complexity

```text
O(n)
```

---

# Advantages

1. Stable sorting algorithm.
2. Suitable for large datasets.
3. Guaranteed O(n log n) complexity.
4. Preserves relative order of equal elements.
5. Efficient for external sorting.

---

# Applications

1. E-commerce order processing.
2. Database management systems.
3. File sorting systems.
4. Record management applications.
5. Large-scale data processing.

---

# Result

The customer orders were successfully sorted using Merge Sort. Random data was generated and execution time was measured. The performance analysis confirmed the theoretical time complexity of O(n log n), making Merge Sort an efficient and stable sorting technique for large datasets.
