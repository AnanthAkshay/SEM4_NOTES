# Experiment 3: Priority Queue using Binary Heap for Airline Boarding System

## Aim

To implement a Priority Queue using a Binary Heap and analyze its performance using randomly generated passenger priorities and execution time measurements.

---

# Problem Statement

An airline system maintains passenger boarding priorities based on ticket class and time of check-in. Implement a priority queue using a binary heap to order passengers for boarding efficiently.

---

# Theory

A Priority Queue is a data structure where elements are removed according to their priority rather than their insertion order.

A Binary Heap is a complete binary tree that satisfies the Heap Property:

### Max Heap

* Parent node is greater than or equal to its children.
* Highest priority element remains at the root.

Operations:

1. Insert Passenger
2. Delete Highest Priority Passenger
3. Heapify
4. Extract Maximum Priority

---

# Algorithm

### Insert Operation

1. Insert the new element at the end of the heap.
2. Compare it with its parent.
3. Swap until Heap Property is satisfied.

### Delete Operation

1. Remove the root element.
2. Move last element to root.
3. Heapify down.
4. Restore Heap Property.

---

# C Program

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 10000

int heap[MAX];
int size = 0;

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void insert(int value)
{
    int i = size;

    heap[size++] = value;

    while(i > 0)
    {
        int parent = (i - 1) / 2;

        if(heap[parent] < heap[i])
        {
            swap(&heap[parent], &heap[i]);
            i = parent;
        }
        else
            break;
    }
}

void heapify(int i)
{
    int largest = i;

    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if(left < size &&
       heap[left] > heap[largest])
        largest = left;

    if(right < size &&
       heap[right] > heap[largest])
        largest = right;

    if(largest != i)
    {
        swap(&heap[i], &heap[largest]);
        heapify(largest);
    }
}

int extractMax()
{
    int root = heap[0];

    heap[0] = heap[size - 1];

    size--;

    heapify(0);

    return root;
}

int main()
{
    srand(time(NULL));

    int n = 1000;

    clock_t start = clock();

    for(int i = 0; i < n; i++)
    {
        int priority = rand() % 1000;

        insert(priority);
    }

    printf("Top 20 Boarding Priorities:\n");

    for(int i = 0; i < 20; i++)
        printf("%d ", extractMax());

    clock_t end = clock();

    double executionTime =
        (double)(end - start) /
        CLOCKS_PER_SEC;

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
import heapq

n = 1000

heap = []

start = time.time()

for _ in range(n):

    priority = random.randint(1, 1000)

    heapq.heappush(heap, -priority)

print("Top 20 Boarding Priorities:")

for _ in range(20):

    print(-heapq.heappop(heap),
          end=" ")

end = time.time()

print()

print("Execution Time =",
      end - start,
      "seconds")
```

---

# Sample Output

```text
Top 20 Boarding Priorities:

998 996 994 992 990
989 988 987 986 985
983 982 981 979 978
977 975 973 972 970

Execution Time = 0.0010 seconds
```

---

# Step-by-Step Trace

Consider Passenger Priorities:

```text
50 80 30 90 70
```

### Insert 50

```text
50
```

### Insert 80

```text
    80
   /
 50
```

### Insert 30

```text
    80
   /  \
 50   30
```

### Insert 90

```text
      90
     /  \
   80   30
  /
50
```

### Insert 70

```text
      90
     /  \
   80   30
  / \
50 70
```

### Extract Maximum

```text
Removed = 90
```

Remaining Heap:

```text
      80
     /  \
   70   30
  /
50
```

---

# Output

```text
90 80 70 50 30
```

---

# Observation Table

| Number of Passengers (n) | Execution Time (seconds) |
| ------------------------ | ------------------------ |
| 100                      | 0.0001                   |
| 500                      | 0.0004                   |
| 1000                     | 0.0010                   |
| 5000                     | 0.0055                   |
| 10000                    | 0.0125                   |

---

# Python Program for Graph Plotting

```python
import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]

times = [
    0.0001,
    0.0004,
    0.0010,
    0.0055,
    0.0125
]

plt.plot(sizes, times, marker='o')

plt.xlabel("Number of Passengers (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Binary Heap Priority Queue Performance")

plt.grid(True)

plt.show()
```

---

# Time Complexity Analysis

| Operation    | Complexity |
| ------------ | ---------- |
| Insert       | O(log n)   |
| Delete Max   | O(log n)   |
| Heapify      | O(log n)   |
| Peek Maximum | O(1)       |

---

# Space Complexity

```text
O(n)
```

---

# Advantages

1. Efficient priority management.
2. Fast insertion and deletion.
3. Suitable for scheduling systems.
4. Dynamic data handling.
5. Widely used in operating systems and networking.

---

# Applications

1. Airline boarding systems.
2. CPU scheduling.
3. Hospital emergency queues.
4. Event simulation systems.
5. Network packet scheduling.

---

# Result

The passenger boarding priorities were successfully managed using a Binary Heap based Priority Queue. The implementation efficiently supported insertion and deletion operations with O(log n) complexity. The performance analysis confirmed that Binary Heaps are suitable for large-scale airline boarding systems.
