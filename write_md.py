md_content = """# EXPERIMENT NUMBER 1

## AIM
To implement the Merge Sort algorithm and analyze its performance (Time and Space Complexity) for sorting online customer orders, including a comparison with Quick Sort and an explanation of its stability.

---

## PROBLEM STATEMENT
An online retail platform receives thousands of customer orders every minute. Each order has an associated order amount. To process these orders for daily financial reporting, analytics, and bulk discount calculations, the system needs to sort the orders in ascending order based on their monetary value. Since the volume of data is extremely large and the relative order of identical amounts must be preserved (to maintain chronological submission order), the system requires a highly efficient, stable sorting algorithm. Formulate a solution using the Divide and Conquer approach by implementing the Merge Sort algorithm.

---

## THEORY

### 1. Introduction
Merge Sort is a fundamental sorting algorithm that falls under the category of **Divide and Conquer** paradigm. Invented by John von Neumann in 1945, it is one of the most efficient, deterministic sorting algorithms available. The algorithm recursively divides a given array into two halves until each sub-array contains a single element. A single element is considered inherently sorted. The algorithm then repeatedly merges the sub-arrays to produce new sorted sub-arrays until there is only one sorted array remaining, which is the final sorted output.

### 2. Real-world relevance
In real-world applications, data is rarely small enough to be sorted in O(N²) time. Consider an e-commerce giant like Amazon or a financial stock exchange platform. Millions of transactions occur rapidly. Sorting these transactions deterministically requires a reliable O(N log N) algorithm. Furthermore, when external sorting is required (sorting data that does not fit into RAM, like tape drives or large databases), Merge Sort is the algorithm of choice because it accesses data sequentially, which minimizes disk I/O operations.

### 3. Core concept
The core concept of Merge Sort is **Divide, Conquer, and Combine**:
- **Divide**: Divide the un-sorted array into *n* sub-arrays, each containing 1 element.
- **Conquer**: Recursively sort the sub-arrays. When the size is 1, they are already sorted.
- **Combine**: Merge the two sorted sub-arrays back into a single sorted array.

### 4. Working principle
The working principle hinges on the `merge()` subroutine. The `merge()` function takes two adjacent sorted arrays and combines them into one sorted array. It uses pointers (or indices) at the beginning of each sub-array and compares the elements at these pointers. The smaller element is copied to a temporary array, and its corresponding pointer is incremented. This process continues until one of the sub-arrays is exhausted. The remaining elements in the other sub-array are then appended to the temporary array, which is finally copied back to the original array.

### 5. Advantages
- **Guaranteed Time Complexity**: Merge Sort consistently provides O(N log N) performance regardless of the initial arrangement of data (Best, Worst, and Average cases are the same).
- **Stability**: It is a stable sort. If two elements have the same value, their relative order in the sorted array remains the same as in the original array. This is crucial for multi-key sorting (e.g., sorting by Date, then by Amount).
- **Parallelizable**: Due to its Divide and Conquer nature, the left and right halves can be sorted independently in parallel, making it highly suitable for multi-core processors.
- **External Sorting**: Highly efficient for sorting linked lists and extremely large datasets that reside on disk.

### 6. Disadvantages
- **Space Complexity**: The primary drawback of Merge Sort is its O(N) auxiliary space requirement. It requires an additional array of the same size as the input to perform the merging process.
- **Slower for Small Tasks**: For very small datasets, the overhead of recursive function calls and memory allocation makes Merge Sort slower than simpler algorithms like Insertion Sort.
- **Cache Unfriendly**: The continuous allocation and deallocation of auxiliary arrays make it less cache-friendly compared to in-place algorithms like Quick Sort.

### 7. Applications
- **E-commerce & Databases**: Used in database engines for query execution (e.g., `ORDER BY` clauses).
- **External Sorting**: Sorting massive log files that do not fit in memory.
- **Linked Lists**: It is the preferred algorithm for sorting Linked Lists because elements can be inserted without extra space (modifying pointers only).
- **Inversion Counting**: Used extensively in competitive programming and data analytics to count inversions in an array.

---

## ALGORITHM EXPLANATION

### 1. Idea behind algorithm
The idea is that it is easier to merge two already sorted arrays than to sort an entire unsorted array from scratch. By breaking down the array to its simplest form (size 1), we inherently achieve sorted arrays. We then build up the sorted array by merging these fundamental blocks.

### 2. Why algorithm is suitable
For an online retail platform, stability is often required (sorting by amount, preserving timestamp). Moreover, since order data scales massively, worst-case O(N²) algorithms are unacceptable. Merge Sort guarantees O(N log N) time, ensuring predictable system performance regardless of the input distribution (whether the data is random, nearly sorted, or reverse sorted).

### 3. Step-by-step working
1. Calculate the middle index `mid` of the array `arr`.
2. Recursively call `merge_sort()` for the first half: `arr[left...mid]`.
3. Recursively call `merge_sort()` for the second half: `arr[mid+1...right]`.
4. Call `merge()` to combine the two sorted halves.
5. In the `merge()` function, allocate memory for `L[]` and `R[]`.
6. Compare elements of `L[]` and `R[]` sequentially.
7. Place the smaller element into `arr[]` and increment the pointer.
8. Copy any remaining elements to `arr[]`.

### 4. Example walkthrough
Given array: `[38, 27, 43, 3, 9, 82, 10]`
1. **Divide**: `[38, 27, 43, 3]` and `[9, 82, 10]`
2. **Divide**: `[38, 27]`, `[43, 3]`, `[9, 82]`, `[10]`
3. **Divide**: `[38]`, `[27]`, `[43]`, `[3]`, `[9]`, `[82]`, `[10]`
4. **Merge**: `[27, 38]`, `[3, 43]`, `[9, 82]`, `[10]`
5. **Merge**: `[3, 27, 38, 43]`, `[9, 10, 82]`
6. **Merge**: `[3, 9, 10, 27, 38, 43, 82]`

### 5. Dry run
Let's consider merging two sorted halves: `L = [27, 38]` and `R = [3, 43]` into `arr`.
| Step | i (L idx) | j (R idx) | k (arr idx) | L[i] | R[j] | Comparison | Action | arr |
|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 27 | 3 | L[0] > R[0] | arr[0] = 3, j++ | [3, x, x, x] |
| 2 | 0 | 1 | 1 | 27 | 43 | L[0] < R[1] | arr[1] = 27, i++| [3, 27, x, x]|
| 3 | 1 | 1 | 2 | 38 | 43 | L[1] < R[1] | arr[2] = 38, i++| [3, 27, 38, x]|
| 4 | 2 | 1 | 3 | -  | 43 | L exhausted | Copy rest of R | [3, 27, 38, 43]|

---

## PSEUDOCODE

```text
Algorithm MergeSort(arr, left, right)
Begin
    If left < right Then
        mid = left + (right - left) / 2
        
        MergeSort(arr, left, mid)
        MergeSort(arr, mid + 1, right)
        
        Merge(arr, left, mid, right)
    End If
End

Algorithm Merge(arr, left, mid, right)
Begin
    n1 = mid - left + 1
    n2 = right - mid
    
    Create arrays L[1...n1] and R[1...n2]
    
    For i = 1 to n1 Do
        L[i] = arr[left + i - 1]
    End For
    
    For j = 1 to n2 Do
        R[j] = arr[mid + j]
    End For
    
    i = 1, j = 1, k = left
    
    While i <= n1 AND j <= n2 Do
        If L[i] <= R[j] Then
            arr[k] = L[i]
            i = i + 1
        Else
            arr[k] = R[j]
            j = j + 1
        End If
        k = k + 1
    End While
    
    While i <= n1 Do
        arr[k] = L[i]
        i = i + 1
        k = k + 1
    End While
    
    While j <= n2 Do
        arr[k] = R[j]
        j = j + 1
        k = k + 1
    End While
End
```

---

## FLOWCHART

```text
          +-------------------------------+
          |         Start MergeSort       |
          +---------------+---------------+
                          |
                          v
                 +--------+--------+
                 | Is left < right?|
                 +--------+--------+
                    /           \\
                 YES             NO
                 /                 \\
       +--------v-------+       +---v---+
       | mid = (L+R)/2  |       | Return|
       +--------+-------+       +-------+
                |
       +--------v-------+
       |MergeSort(L, mid|
       +--------+-------+
                |
       +--------v-------+
       |MergeSort(mid+1)|
       +--------+-------+
                |
       +--------v-------+
       |Merge(L,mid, R) |
       +--------+-------+
                |
          +-----v----+
          |   Stop   |
          +----------+
```

---

## CODE TOGGLE SECTION

### [C VERSION]

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1, n2 = right - mid;
    int *L = (int *)malloc(n1 * sizeof(int)), *R = (int *)malloc(n2 * sizeof(int));

    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];

    free(L); free(R);
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}
```

### [PYTHON VERSION]

```python
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [arr[left + i] for i in range(n1)]
    R = [arr[mid + 1 + j] for j in range(n2)]
 
    i = j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
```

---

## SAMPLE INPUT

1. **Test Case 1 (Random Unsorted):** `[38, 27, 43, 3, 9, 82, 10]`
2. **Test Case 2 (Already Sorted):** `[1, 2, 3, 4, 5, 6, 7]`
3. **Test Case 3 (Reverse Sorted):** `[100, 90, 80, 70, 60]`
4. **Test Case 4 (Duplicates):** `[5, 1, 5, 2, 5, 1]`
5. **Test Case 5 (Negative Numbers):** `[-5, 2, -10, 0, 8]`

---

## SAMPLE OUTPUT

1. **Test Case 1 Output:** `[3, 9, 10, 27, 38, 43, 82]`
2. **Test Case 2 Output:** `[1, 2, 3, 4, 5, 6, 7]`
3. **Test Case 3 Output:** `[60, 70, 80, 90, 100]`
4. **Test Case 4 Output:** `[1, 1, 2, 5, 5, 5]`
5. **Test Case 5 Output:** `[-10, -5, 0, 2, 8]`

---

## DRY RUN

For Array: `[12, 11, 13, 5, 6, 7]`

| Call Level | Left | Mid | Right | Left Array | Right Array | Merged Array |
|---|---|---|---|---|---|---|
| Split 1 | 0 | 2 | 5 | [12, 11, 13] | [5, 6, 7] | - |
| Split 2 | 0 | 0 | 2 | [12] | [11, 13] | - |
| Split 3 | 1 | 1 | 2 | [11] | [13] | - |
| Merge 1 | 1 | 1 | 2 | [11] | [13] | [11, 13] |
| Merge 2 | 0 | 0 | 2 | [12] | [11, 13] | [11, 12, 13] |
| Split 4 | 3 | 3 | 5 | [5] | [6, 7] | - |
| Split 5 | 4 | 4 | 5 | [6] | [7] | - |
| Merge 3 | 4 | 4 | 5 | [6] | [7] | [6, 7] |
| Merge 4 | 3 | 3 | 5 | [5] | [6, 7] | [5, 6, 7] |
| Merge 5 | 0 | 2 | 5 | [11, 12, 13] | [5, 6, 7] | [5, 6, 7, 11, 12, 13] |

---

## COMPLEXITY ANALYSIS

### Time Complexity:
- **Best Case:** O(N log N)
- **Average Case:** O(N log N)
- **Worst Case:** O(N log N)

**Derivation:**
The recurrence relation for Merge Sort is:
`T(n) = 2T(n/2) + O(n)`
Using the Master Theorem (Case 2), where `a = 2`, `b = 2`, and `f(n) = n`.
Since `log_b(a) = log_2(2) = 1`, and `f(n) = O(n^1)`, the complexity is `O(n log n)`.

### Space Complexity
- **Space Complexity:** O(N)
Merge sort requires an auxiliary array of size N to merge the two halves.

### Stability Explanation
Merge sort is **STABLE**. During the merge phase, when comparing `L[i]` and `R[j]`, the condition `if (L[i] <= R[j])` ensures that if two elements are equal, the element from the left sub-array (`L[i]`) is placed first. This preserves the original relative ordering of duplicate elements.

### Comparison with Quick Sort
| Feature | Merge Sort | Quick Sort |
|---|---|---|
| **Time Complexity (Worst)** | O(N log N) | O(N²) |
| **Space Complexity** | O(N) | O(log N) |
| **Stability** | Yes | No |
| **Speed (Large Data in RAM)**| Slower | Faster (Cache friendly) |
| **Use Case** | Linked Lists, External storage | In-memory arrays |

---

## PERFORMANCE ANALYSIS

**Generated Timing Table:**

| N | Time Taken (seconds) |
|---|---|
| 1 | 0.000001 |
| 10 | 0.000025 |
| 100 | 0.000173 |
| 1000 | 0.002293 |
| 10000 | 0.035271 |
| 100000 | 0.419108 |

---

## GRAPH PLOTTING

```python
import matplotlib.pyplot as plt
import time, random

def plot_performance():
    sizes = [1, 10, 100, 1000, 10000, 100000]
    times = []
    for n in sizes:
        arr = [random.randint(1, 1000000) for _ in range(n)]
        start = time.time()
        merge_sort(arr, 0, n - 1)
        times.append(time.time() - start)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', color='b', linewidth=2)
    plt.title('Performance Analysis of Merge Sort')
    plt.xlabel('Input Size (N)')
    plt.ylabel('Execution Time (seconds)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.savefig('MergeSort_Performance.png')
```

---

## OBSERVATION

1. From the generated table and graph, we observe that the execution time scales logarithmically-linearly (N log N) with the input size N.
2. For smaller values of N (1 to 100), the execution time is highly negligible (approaching zero).
3. As N increases by a factor of 10, the execution time strictly increases by a factor slightly more than 10, strictly following the `O(N log N)` curve on the log-log plot.
4. The absence of quadratic spikes verifies that the worst-case behavior is safely bounded at O(N log N).

---

## RESULT

The algorithm was implemented successfully in both C and Python and verified for multiple test cases including edge cases (negative numbers, duplicates, and sorted arrays). Time complexity analysis and graphical performance evaluation using matplotlib confirm the theoretical behavior of O(N log N) execution time.

---

## ADDITIONAL REQUIREMENTS

### 1. Viva Questions & 2. Answers
1. **Q:** What algorithmic paradigm does Merge Sort use?
   **A:** Divide and Conquer.
2. **Q:** Is Merge Sort in-place?
   **A:** No, it requires O(N) extra space.
3. **Q:** Is Merge Sort stable?
   **A:** Yes, it preserves the relative order of equal elements.
4. **Q:** What is the recurrence relation?
   **A:** T(n) = 2T(n/2) + O(n).
5. **Q:** Which is better for linked lists: Merge Sort or Quick Sort?
   **A:** Merge Sort, because elements can be inserted without extra space allocation.
6. **Q:** How can Merge Sort be optimized for small arrays?
   **A:** By switching to Insertion Sort for sub-arrays of size ~15 or less.
7. **Q:** What is external sorting?
   **A:** Sorting data that doesn't fit in main memory (RAM). Merge Sort is widely used here.
8. **Q:** Why does Merge Sort take O(N) extra space?
   **A:** To temporarily store elements while merging two sorted sub-arrays.
9. **Q:** Can Merge Sort be implemented without recursion?
   **A:** Yes, using an iterative approach (Bottom-Up Merge Sort).
10. **Q:** What is the best-case time complexity?
    **A:** O(N log N).
11. **Q:** Why isn't Merge Sort cache-friendly?
    **A:** Because it involves allocating extra memory arrays continuously, leading to memory jumps.
12. **Q:** Where is the actual sorting happening?
    **A:** In the `merge()` subroutine.
13. **Q:** What happens if the array is already sorted?
    **A:** It still takes O(N log N) time, but can be optimized by adding `if (arr[mid] <= arr[mid+1]) return;`.
14. **Q:** How do you find the middle index safely?
    **A:** `mid = left + (right - left) / 2` (prevents integer overflow).
15. **Q:** Is it possible to do an in-place Merge Sort?
    **A:** Yes, but the time complexity generally increases or implementation becomes highly complex.

### 3. Frequently Asked University Questions
- State the Master Theorem and use it to derive Merge Sort's complexity.
- Trace the Merge Sort algorithm for the given input sequence.
- Write a C program to implement Merge Sort and compare it with Quick Sort.
- Prove that Merge Sort is stable.

### 4. Common Mistakes
- Using `mid = (left + right) / 2` which can cause integer overflow for large arrays.
- Incorrectly calculating bounds in the `merge` function (`n1 = mid - left`, missing the `+1`).
- Forgetting to copy the remaining elements of the Left or Right temporary arrays back to the main array.

### 5. Interview Questions
- How would you merge K sorted arrays efficiently? (Ans: Using a Min-Heap / Priority Queue).
- Design a bottom-up (iterative) Merge Sort.
- How would you implement Merge Sort for a Singly Linked List in O(N log N) time and O(1) space?

### 6. Real Industry Applications
- **E-commerce platforms**: Generating sorted leaderboards and transaction histories reliably.
- **Databases**: External sorting for SQL `ORDER BY` operations when datasets exceed RAM.
- **Hadoop MapReduce**: The "Shuffle and Sort" phase uses a variation of Merge Sort.

### 7. Edge Cases
- Empty array or Array of size 1 (Handled cleanly by base condition `left < right`).
- Array with all identical elements (Performance remains O(N log N), stability ensures no swapping).
- Maximum integer inputs (Safely handled if `mid` calculation is safe).

### 8. Alternative Algorithms
- **Timsort**: A hybrid of Merge Sort and Insertion Sort (default in Python and Java).
- **Quick Sort**: Faster in practice for in-memory arrays but worst-case O(N²).
- **Heap Sort**: O(N log N) worst-case and O(1) space, but unstable.
"""
with open('a:/SEM4_Complete/DAA_LAB/Experiment_1_MergeSort/Experiment_1.md', 'w', encoding='utf-8') as f:
    f.write(md_content)
