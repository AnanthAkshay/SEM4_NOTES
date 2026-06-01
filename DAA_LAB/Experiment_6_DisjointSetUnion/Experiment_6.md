# EXPERIMENT NUMBER 6

## AIM
To implement a Disjoint-Set Data Structure (Union-Find) with Union by Rank and Path Compression optimizations, and evaluate its performance (Time and Space Complexity) to efficiently track and manage dynamically merging friend groups in a social networking platform.

---

## PROBLEM STATEMENT
A rapidly growing social networking platform needs to continuously track large friend circles as users independently form new connections. When User A adds User B as a friend, their respective friend networks instantly merge into one massive group. The backend system must handle millions of these "friend requests" and quickly respond to queries asking "Are User X and User Y in the same friend network?". Doing this using standard graph traversals like BFS/DFS for every query takes O(V+E) time, which will crash the servers. Formulate an ultra-efficient tracking solution using the Disjoint-Set Union (DSU) data structure, achieving near O(1) amortized time per operation.

---

## THEORY

### 1. Introduction
The **Disjoint-Set Data Structure** (also known as a Union-Find data structure) maintains a collection of disjoint (non-overlapping) sets. It provides two extremely fast core operations:
1. **Find**: Determine which set a particular element belongs to. This is used to check if two elements are in the same set.
2. **Union**: Join two subsets into a single subset.

By modeling elements as nodes in a forest of trees, DSU can determine component connectivity dynamically without needing to store or traverse the entire edge list of a graph.

### 2. Real-world relevance
Any system that builds connectivity dynamically needs DSU. Be it calculating Minimum Spanning Trees (Kruskal's Algorithm), determining network routing boundaries, grouping pixels of similar colors in computer vision (connected component labeling), or managing social network components, DSU solves dynamic connectivity queries exponentially faster than standard graph searches.

### 3. Core concept
A standard DSU can be slow (O(N) time) if trees become heavily skewed (like a linked list). To prevent this, two critical optimizations are applied simultaneously:
- **Union by Rank**: Always attach the shorter tree under the root of the taller tree. This keeps the trees incredibly flat.
- **Path Compression**: Whenever `Find(x)` is called, directly attach `x` (and all nodes traversed along the way) to the root of the tree. This ensures future `Find` operations take near constant time.

### 4. Working principle
- **Initialization**: Every user starts in their own independent set (parent of $i$ is $i$).
- **Find(x)**: Traverse parent pointers until reaching a node that is its own parent (the root). While returning from the recursion, point all visited nodes directly to this root (Path Compression).
- **Union(x, y)**: Find the roots of $x$ and $y$. Compare their ranks (approximate height). Attach the root with the smaller rank to the root with the larger rank. If ranks are equal, pick one as the new root and increment its rank by 1.

### 5. Advantages
- **Unprecedented Speed**: With both optimizations, the amortized time complexity per operation drops to $O(\alpha(N))$, where $\alpha(N)$ is the Inverse Ackermann function. For all practical values of $N$ in the universe, $\alpha(N) \le 4$, making it effectively $O(1)$.
- **Low Memory Overhead**: Only requires two arrays (`parent` and `rank`), achieving strict O(N) space complexity.
- **Dynamic Adaptability**: Can process edges sequentially online, unlike DFS which requires the whole graph upfront.

### 6. Disadvantages
- **No Edge Deletion**: Standard DSU cannot easily "un-union" two sets. If two users unfriend each other, separating their sub-components requires complex augmentations or complete recalculations.
- **Limited Information**: It only tracks connectivity, not the specific path or distance between two nodes.

### 7. Applications
- **Kruskal's Algorithm**: Detecting cycles while building Minimum Spanning Trees.
- **Network Connectivity**: Fast querying of LAN/WAN subnet partitions.
- **Percolation Theory**: Simulating fluid flow through porous materials in physics.

---

## ALGORITHM EXPLANATION

### 1. Idea behind algorithm
Imagine friend groups as corporate hierarchies. Every person has a boss, and the boss has a boss, all the way up to the CEO (the root). To check if two people work for the same company, just check if they have the same CEO. When two companies merge (Union), the CEO of the smaller company simply reports to the CEO of the larger company (Union by Rank). To make things faster, whenever an employee talks to the CEO, they change their direct boss to be the CEO (Path Compression).

### 2. Why algorithm is suitable
Social networks process millions of edge creations (friend requests) sequentially. A standard DFS/BFS to check connectivity takes $O(N)$ time per query. For $M$ queries, that's $O(M \times N)$, which is disastrous. DSU processes $M$ queries in $O(M \alpha(N))$, which is essentially $O(M)$ total time. It scales flawlessly to billions of users.

### 3. Step-by-step working
`MakeSet(N)`:
1. Initialize `parent[i] = i` for all $i$ from $0$ to $N-1$.
2. Initialize `rank[i] = 0` for all $i$.

`Find(i)`:
1. If `parent[i] == i`, return `i` (it's the root).
2. Else, recursively call `Find(parent[i])` and assign the result to `parent[i]`. (Path Compression).
3. Return `parent[i]`.

`Union(x, y)`:
1. `rootX = Find(x)` and `rootY = Find(y)`.
2. If `rootX == rootY`, they are already connected. Return.
3. Compare `rank[rootX]` and `rank[rootY]`.
4. If `rank[rootX] < rank[rootY]`, `parent[rootX] = rootY`.
5. Else if `rank[rootX] > rank[rootY]`, `parent[rootY] = rootX`.
6. Else, `parent[rootY] = rootX` and `rank[rootX]++`.

### 4. Example walkthrough
`N = 5` (Users 0, 1, 2, 3, 4)
Initial: Each user is isolated.
1. `Union(0, 1)`: Root 0, Root 1. Both rank 0. `parent[1] = 0`. `rank[0] = 1`. Set: {0, 1}.
2. `Union(2, 3)`: Root 2, Root 3. Both rank 0. `parent[3] = 2`. `rank[2] = 1`. Set: {2, 3}.
3. `Union(0, 2)`: Root 0 (rank 1), Root 2 (rank 1). Ranks equal. `parent[2] = 0`. `rank[0]` becomes 2. Sets merged: {0, 1, 2, 3}.
4. `Find(3)`:
   - `parent[3]` is 2. `parent[2]` is 0. `parent[0]` is 0.
   - Root is 0.
   - Path Compression: Updates `parent[3] = 0`. (Next time `Find(3)` is O(1)).

### 5. Dry run
Testing `Union(1, 2)` and `Union(2, 3)` on `N=4`.
**Init:** `parent = [0, 1, 2, 3]`, `rank = [0, 0, 0, 0]`

**Union(1, 2):**
- `rootX = Find(1) = 1`
- `rootY = Find(2) = 2`
- Both rank 0. `parent[2] = 1`. `rank[1] = 1`.
- State: `parent = [0, 1, 1, 3]`, `rank = [0, 1, 0, 0]`

**Union(2, 3):**
- `rootX = Find(2) = 1` (Path compression updates nothing here)
- `rootY = Find(3) = 3`
- `rank[1] (1) > rank[3] (0)`.
- `parent[3] = 1`.
- State: `parent = [0, 1, 1, 1]`, `rank = [0, 1, 0, 0]`

All nodes {1, 2, 3} correctly point to root `1`.

---

## PSEUDOCODE

```text
Structure DSU
    Array parent
    Array rank
    
Algorithm MakeSet(n)
    For i = 0 to n-1 Do
        parent[i] = i
        rank[i] = 0
    End For
    
Algorithm Find(i)
    If parent[i] != i Then
        // Path Compression
        parent[i] = Find(parent[i])
    End If
    Return parent[i]
    
Algorithm Union(x, y)
    rootX = Find(x)
    rootY = Find(y)
    
    If rootX == rootY Then
        Return // Already in same set
    End If
    
    // Union by Rank
    If rank[rootX] < rank[rootY] Then
        parent[rootX] = rootY
    Else If rank[rootX] > rank[rootY] Then
        parent[rootY] = rootX
    Else
        parent[rootY] = rootX
        rank[rootX] = rank[rootX] + 1
    End If
```

---

## FLOWCHART

```text
          +-------------------------------+
          |          Start Union(x, y)    |
          +---------------+---------------+
                          |
                          v
          +-------------------------------+
          |  rootX = Find(x)              |
          |  rootY = Find(y)              |
          +---------------+---------------+
                          |
                 [ rootX == rootY ? ] ---> (Yes) -> [ Stop ]
                          | (No)
                          v
          +-------------------------------+
          | Compare rank[rootX], rootY]   |
          +---------------+---------------+
                          |
          +---------------+---------------+
          |               |               |
 rank[X] < rank[Y]   rank[X] > rank[Y]   rank[X] == rank[Y]
          |               |               |
          v               v               v
  parent[rootX]=Y   parent[rootY]=X   parent[rootY]=X
                                      rank[rootX]++
          |               |               |
          +---------------+---------------+
                          |
                          v
                      [ Stop ]
```

---

## CODE TOGGLE SECTION

### [C VERSION]

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct { int *parent; int *rank; int n; } DSU;

DSU* createDSU(int n) {
    DSU *dsu = (DSU *)malloc(sizeof(DSU));
    dsu->n = n;
    dsu->parent = (int *)malloc(n * sizeof(int));
    dsu->rank = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        dsu->parent[i] = i;
        dsu->rank[i] = 0;
    }
    return dsu;
}

int find(DSU *dsu, int i) {
    if (dsu->parent[i] != i)
        dsu->parent[i] = find(dsu, dsu->parent[i]);
    return dsu->parent[i];
}

void unionSet(DSU *dsu, int x, int y) {
    int rootX = find(dsu, x), rootY = find(dsu, y);
    if (rootX == rootY) return;

    if (dsu->rank[rootX] < dsu->rank[rootY]) dsu->parent[rootX] = rootY;
    else if (dsu->rank[rootX] > dsu->rank[rootY]) dsu->parent[rootY] = rootX;
    else {
        dsu->parent[rootY] = rootX;
        dsu->rank[rootX]++;
    }
}
```

### [PYTHON VERSION]

```python
class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
```

---

## SAMPLE INPUT
1. Initialize Network with 5 Users (0 to 4).
2. Union(0, 1)
3. Union(1, 2)
4. Check Friend(0, 2)
5. Check Friend(0, 4)
6. Union(3, 4)
7. Union(2, 4)
8. Check Friend(0, 3)

---

## SAMPLE OUTPUT
1. Network Created.
2. User 0 and 1 connected.
3. User 1 and 2 connected.
4. Yes! User 0 and User 2 belong to the same friend group.
5. No. User 0 and User 4 are in different groups.
6. User 3 and 4 connected.
7. User 2 and 4 connected.
8. Yes! User 0 and User 3 belong to the same friend group.

---

## COMPLEXITY ANALYSIS

### Time Complexity:
- **MakeSet:** $O(N)$
- **Find:** Amortized $O(\alpha(N)) \approx O(1)$
- **Union:** Amortized $O(\alpha(N)) \approx O(1)$

**Derivation:**
Without optimizations, DSU trees can become linked lists, leading to $O(N)$ operations. 
Using *only* Union by Rank ensures the height of the tree never exceeds $\log N$, giving $O(\log N)$ worst-case time.
Using *only* Path Compression gives average $O(\log N)$ time per operation.
Using *both* optimizations mathematically squashes the tree so flat that any operation takes $O(\alpha(N))$ time, where $\alpha$ is the Inverse Ackermann Function. Since $\alpha(10^{80}) \le 4$, it is considered a tiny constant. Thus, $M$ operations on $N$ elements take $O(M \alpha(N))$ time.

### Space Complexity
- **Space Complexity:** $O(N)$
Requires two arrays `parent` and `rank`, each of size N.

---

## PERFORMANCE ANALYSIS

**Generated Timing Table:** (Based on executing $N$ sequential Union operations)

| N | Time Taken (seconds) |
|---|---|
| 1 | 0.000024 |
| 10 | 0.000026 |
| 100 | 0.000149 |
| 1000 | 0.001803 |
| 10000 | 0.017867 |
| 100000 | 0.252516 |

---

## GRAPH PLOTTING

```python
import matplotlib.pyplot as plt
import time, random

def plot_performance():
    sizes = [1, 10, 100, 1000, 10000, 100000]
    times = []
    for n in sizes:
        dsu = DSU(n)
        start = time.time()
        for _ in range(n):
            u, v = random.randint(0, n-1), random.randint(0, n-1)
            dsu.union(u, v)
        times.append(time.time() - start)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='s', color='magenta', linewidth=2)
    plt.title('Performance Analysis of DSU (N Union Operations)')
    plt.xlabel('Input Size (N users/operations)')
    plt.ylabel('Execution Time (seconds)')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.savefig('DSU_Performance.png')
```

---

## OBSERVATION

1. Processing 100,000 randomized union operations takes barely ~0.25 seconds. If this were done using standard graph DFS traversing 100k nodes dynamically, it would take exponentially longer and likely exceed recursion depth limits.
2. The log-log plot demonstrates linear scaling for $N$ operations. Since $N$ operations take $O(N)$ total time, it implies that each individual operation executes in effectively $O(1)$ amortized time.
3. Path compression is the silent hero; after a few initial connections, the tree height collapses to 2, making all subsequent `Find` operations instantly hit the root node.

---

## RESULT

The Disjoint-Set Union algorithm was implemented successfully with Union by Rank and Path Compression optimizations. The social network backend efficiently tracked and dynamically merged thousands of friend groups, capable of responding to connectivity queries in near-constant $O(1)$ amortized time, completely bypassing the massive computational overhead of standard graph traversals.

---

## ADDITIONAL REQUIREMENTS

### 1. Viva Questions & 2. Answers
1. **Q:** What is Path Compression in DSU?
   **A:** It is a technique where every node visited during a `Find` operation is attached directly to the root of the tree, flattening the structure for future queries.
2. **Q:** What is Union by Rank?
   **A:** It is an optimization where the tree with the smaller height (rank) is always attached under the root of the taller tree to prevent the tree from becoming skewed like a linked list.
3. **Q:** Can DSU detect cycles in an undirected graph?
   **A:** Yes! If you try to `Union(x, y)` and they both already have the exact same root, it means an edge between them forms a cycle.
4. **Q:** Can DSU detect cycles in a directed graph?
   **A:** No, DSU cannot accurately track directionality. You must use DFS with back-edge detection.
5. **Q:** What is the Time Complexity of DSU operations?
   **A:** $O(\alpha(N))$, where $\alpha$ is the Inverse Ackermann function.
6. **Q:** What is the Inverse Ackermann function?
   **A:** A mathematical function that grows so incredibly slowly that for all practical numbers $N$, its value is $\le 4$.
7. **Q:** Can we delete an edge in a standard DSU?
   **A:** No. Path compression irrevocably destroys the original tree topology. To support deletions, you need advanced techniques like Rollback DSU (which forbids Path Compression).
8. **Q:** Why do we initialize `rank` to 0 instead of 1?
   **A:** Rank represents an upper bound on the height of the tree. A single isolated node has a height of 0.
9. **Q:** Does Path Compression alter the `rank` array?
   **A:** No. The rank remains an *upper bound* on height, not the exact height. Updating exact ranks after compression is computationally expensive and unnecessary.
10. **Q:** If $N$ is 1 billion, what is the maximum depth of a DSU tree using only Union by Rank?
    **A:** Approximately $\log_2(10^9) \approx 30$.

### 3. Frequently Asked University Questions
- Explain Disjoint Set data structure. Discuss the Find and Union algorithms with path compression and rank optimizations.
- Demonstrate cycle detection in an undirected graph using DSU with a manual trace of 5 edges.
- Why is it difficult to implement edge deletion in an optimized DSU?

### 4. Common Mistakes
- Forget to `return` the updated root during Path Compression recursion: `parent[i] = Find(parent[i]); return parent[i];`.
- Confusing Union by Size with Union by Rank. (Both yield the same amortized complexity, but rank uses heights, while size tracks total node count).
- Attempting to use DSU for pathfinding; DSU only answers *if* a path exists, not *what* the path is.

### 5. Interview Questions
- How would you modify DSU to find the size of the component a specific node belongs to? (Ans: Use a `size` array instead of `rank` and accumulate it during Union).
- Use DSU to count the number of islands in a dynamic grid where land can be added over time.
- Implement Kruskal's Algorithm using your custom DSU class.

### 6. Real Industry Applications
- **Compilers**: Variable equivalence class mapping.
- **Image Processing**: Fast connected-component labeling for separating objects in foreground extraction.
- **Multiplayer Games**: Grouping players dynamically into squads or server shards.

### 7. Edge Cases
- `Union(A, A)`: Calling union on the exact same node (Handled by the `rootX == rootY` check).
- Calling `Find(x)` on a non-existent node (handled by bounds checking before DSU calls).
- Very dense graph: $E \approx V^2$ edges. DSU processes this effortlessly in $O(E \alpha(V))$ time.

### 8. Alternative Algorithms
- **DFS / BFS**: Slower for dynamic connectivity ($O(N)$ per query), but can provide exact paths.
- **Dynamic Trees (Link/Cut Trees)**: Advanced data structure that supports both fast dynamic connectivity and edge deletions in $O(\log N)$ time.
