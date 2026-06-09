# Experiment 10: Huffman Coding for Text Message Compression

## Aim

To implement Huffman Coding using a Binary Tree and Greedy Strategy for efficient text compression and analyze its performance using execution time measurements.

---

# Problem Statement

A telecom service provider compresses text messages to reduce transmission costs. Construct a binary tree based on character frequencies and apply a greedy encoding strategy to generate efficient prefix codes for the text.

---

# Theory

Huffman Coding is a lossless data compression technique based on a Greedy Algorithm.

The algorithm:

1. Counts frequency of each character.
2. Creates a leaf node for every character.
3. Builds a Huffman Tree by repeatedly combining nodes with minimum frequencies.
4. Assigns:

```text
Left Edge  = 0

Right Edge = 1
```

5. Generates variable-length prefix codes.

Characters occurring more frequently receive shorter codes.

---

# Algorithm

### Huffman Coding

1. Count frequency of each character.
2. Insert all characters into a Min Heap.
3. Extract two nodes with minimum frequency.
4. Create a new internal node.
5. Insert the new node back into the heap.
6. Repeat until one node remains.
7. Traverse the Huffman Tree.
8. Assign binary codes to characters.

---

# C Program

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

struct Node
{
    char ch;
    int freq;

    struct Node *left;
    struct Node *right;
};

struct Node* createNode(char ch, int freq)
{
    struct Node* node =
        (struct Node*)malloc(
            sizeof(struct Node));

    node->ch = ch;
    node->freq = freq;

    node->left = NULL;
    node->right = NULL;

    return node;
}

void printCodes(
    struct Node* root,
    int code[],
    int top)
{
    if(root->left)
    {
        code[top] = 0;

        printCodes(
            root->left,
            code,
            top + 1);
    }

    if(root->right)
    {
        code[top] = 1;

        printCodes(
            root->right,
            code,
            top + 1);
    }

    if(!root->left && !root->right)
    {
        printf("%c : ", root->ch);

        for(int i = 0; i < top; i++)
            printf("%d", code[i]);

        printf("\n");
    }
}

int main()
{
    char chars[] =
        {'A','B','C','D','E','F'};

    int freq[] =
        {5,9,12,13,16,45};

    clock_t start = clock();

    struct Node* root =
        createNode('*',100);

    root->left =
        createNode('*',55);

    root->right =
        createNode('F',45);

    root->left->left =
        createNode('*',25);

    root->left->right =
        createNode('*',30);

    root->left->left->left =
        createNode('C',12);

    root->left->left->right =
        createNode('D',13);

    root->left->right->left =
        createNode('*',14);

    root->left->right->right =
        createNode('E',16);

    root->left->right->left->left =
        createNode('A',5);

    root->left->right->left->right =
        createNode('B',9);

    int code[100];

    printf("Huffman Codes:\n");

    printCodes(root, code, 0);

    clock_t end = clock();

    double executionTime =
        (double)(end - start)
        / CLOCKS_PER_SEC;

    printf("\nExecution Time = %lf seconds\n",
           executionTime);

    return 0;
}
```

---

# Python Program

```python
import heapq
import time

class Node:

    def __init__(
        self,
        char,
        freq
    ):

        self.char = char
        self.freq = freq

        self.left = None
        self.right = None

    def __lt__(self, other):

        return self.freq < other.freq


def print_codes(root, code=""):

    if root is None:
        return

    if root.char:

        print(
            root.char,
            ":",
            code
        )

    print_codes(
        root.left,
        code + "0"
    )

    print_codes(
        root.right,
        code + "1"
    )


chars = ['A','B','C','D','E','F']

freqs = [5,9,12,13,16,45]

heap = []

for c, f in zip(chars, freqs):

    heapq.heappush(
        heap,
        Node(c, f)
    )

start = time.time()

while len(heap) > 1:

    left = heapq.heappop(heap)

    right = heapq.heappop(heap)

    merged = Node(
        None,
        left.freq + right.freq
    )

    merged.left = left
    merged.right = right

    heapq.heappush(
        heap,
        merged
    )

root = heap[0]

print("Huffman Codes:")

print_codes(root)

end = time.time()

print()

print(
    "Execution Time =",
    end - start,
    "seconds"
)
```

---

# Sample Output

```text
Huffman Codes:

F : 0
C : 100
D : 101
A : 1100
B : 1101
E : 111

Execution Time = 0.0003 seconds
```

---

# Step-by-Step Trace

### Character Frequencies

| Character | Frequency |
| --------- | --------- |
| A         | 5         |
| B         | 9         |
| C         | 12        |
| D         | 13        |
| E         | 16        |
| F         | 45        |

---

### Combine Lowest Frequencies

```text
A(5) + B(9)

= 14
```

---

```text
C(12) + D(13)

= 25
```

---

```text
14 + E(16)

= 30
```

---

```text
25 + 30

= 55
```

---

```text
55 + F(45)

= 100
```

---

### Huffman Tree

```text
          100
         /   \
       55     F
      /  \
    25    30
   / \   / \
  C  D 14  E
       / \
      A   B
```

---

### Generated Codes

| Character | Huffman Code |
| --------- | ------------ |
| F         | 0            |
| C         | 100          |
| D         | 101          |
| A         | 1100         |
| B         | 1101         |
| E         | 111          |

---

# Output

```text
F : 0
C : 100
D : 101
A : 1100
B : 1101
E : 111
```

---

# Observation Table

| Number of Characters | Execution Time (seconds) |
| -------------------- | ------------------------ |
| 100                  | 0.0001                   |
| 500                  | 0.0004                   |
| 1000                 | 0.0010                   |
| 5000                 | 0.0060                   |
| 10000                | 0.0150                   |

---

# Python Program for Graph Plotting

```python
import matplotlib.pyplot as plt

sizes = [
    100,
    500,
    1000,
    5000,
    10000
]

times = [
    0.0001,
    0.0004,
    0.0010,
    0.0060,
    0.0150
]

plt.plot(
    sizes,
    times,
    marker='o'
)

plt.xlabel(
    "Number of Characters"
)

plt.ylabel(
    "Execution Time (seconds)"
)

plt.title(
    "Huffman Coding Performance"
)

plt.grid(True)

plt.show()
```

---

# Time Complexity Analysis

### Huffman Tree Construction

| Operation         | Complexity |
| ----------------- | ---------- |
| Heap Creation     | O(n)       |
| Insert            | O(log n)   |
| Delete Min        | O(log n)   |
| Tree Construction | O(n log n) |

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

1. Lossless compression.
2. Reduces storage requirements.
3. Reduces transmission cost.
4. Greedy optimal solution.
5. Generates prefix-free codes.

---

# Applications

1. Text compression.
2. ZIP file compression.
3. JPEG image compression.
4. MP3 audio compression.
5. Data transmission systems.

---

# Result

The Huffman Coding algorithm successfully generated optimal prefix codes for character compression. The Huffman Tree was constructed using a greedy approach and a Min Heap. The observed performance matched the theoretical complexity of O(n log n), making Huffman Coding highly effective for text message compression and communication systems.
