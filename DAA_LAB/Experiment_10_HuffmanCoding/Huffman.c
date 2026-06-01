#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_TREE_HT 100
#define MAX_CHAR 256

// A Huffman tree node
struct MinHeapNode {
    char data;
    unsigned freq;
    struct MinHeapNode *left, *right;
};

// A Min Heap: Collection of min-heap nodes
struct MinHeap {
    unsigned size;
    unsigned capacity;
    struct MinHeapNode **array;
};

// Helper function to allocate a new tree node
struct MinHeapNode* newNode(char data, unsigned freq) {
    struct MinHeapNode* temp = (struct MinHeapNode*)malloc(sizeof(struct MinHeapNode));
    temp->left = temp->right = NULL;
    temp->data = data;
    temp->freq = freq;
    return temp;
}

// Helper function to create a min heap of given capacity
struct MinHeap* createMinHeap(unsigned capacity) {
    struct MinHeap* minHeap = (struct MinHeap*)malloc(sizeof(struct MinHeap));
    minHeap->size = 0;
    minHeap->capacity = capacity;
    minHeap->array = (struct MinHeapNode**)malloc(minHeap->capacity * sizeof(struct MinHeapNode*));
    return minHeap;
}

// Utility function to swap two min heap nodes
void swapMinHeapNode(struct MinHeapNode** a, struct MinHeapNode** b) {
    struct MinHeapNode* t = *a;
    *a = *b;
    *b = t;
}

// The standard minHeapify function.
void minHeapify(struct MinHeap* minHeap, int idx) {
    int smallest = idx;
    int left = 2 * idx + 1;
    int right = 2 * idx + 2;

    if (left < minHeap->size && minHeap->array[left]->freq < minHeap->array[smallest]->freq)
        smallest = left;

    if (right < minHeap->size && minHeap->array[right]->freq < minHeap->array[smallest]->freq)
        smallest = right;

    if (smallest != idx) {
        swapMinHeapNode(&minHeap->array[smallest], &minHeap->array[idx]);
        minHeapify(minHeap, smallest);
    }
}

// Utility function to check if size of heap is 1
int isSizeOne(struct MinHeap* minHeap) {
    return (minHeap->size == 1);
}

// Standard function to extract minimum value node from heap
struct MinHeapNode* extractMin(struct MinHeap* minHeap) {
    struct MinHeapNode* temp = minHeap->array[0];
    minHeap->array[0] = minHeap->array[minHeap->size - 1];
    --minHeap->size;
    minHeapify(minHeap, 0);
    return temp;
}

// Utility function to insert a new node to Min Heap
void insertMinHeap(struct MinHeap* minHeap, struct MinHeapNode* minHeapNode) {
    ++minHeap->size;
    int i = minHeap->size - 1;

    while (i && minHeapNode->freq < minHeap->array[(i - 1) / 2]->freq) {
        minHeap->array[i] = minHeap->array[(i - 1) / 2];
        i = (i - 1) / 2;
    }
    minHeap->array[i] = minHeapNode;
}

// Standard function to build min heap
void buildMinHeap(struct MinHeap* minHeap) {
    int n = minHeap->size - 1;
    for (int i = (n - 1) / 2; i >= 0; --i)
        minHeapify(minHeap, i);
}

// Utility function to check if this node is leaf
int isLeaf(struct MinHeapNode* root) {
    return !(root->left) && !(root->right);
}

// Creates a min heap and inserts all characters of data[] and freq[]
struct MinHeap* createAndBuildMinHeap(char data[], int freq[], int size) {
    struct MinHeap* minHeap = createMinHeap(size);
    for (int i = 0; i < size; ++i)
        minHeap->array[i] = newNode(data[i], freq[i]);
    minHeap->size = size;
    buildMinHeap(minHeap);
    return minHeap;
}

// The main function that builds Huffman tree
struct MinHeapNode* buildHuffmanTree(char data[], int freq[], int size) {
    struct MinHeapNode *left, *right, *top;
    struct MinHeap* minHeap = createAndBuildMinHeap(data, freq, size);

    while (!isSizeOne(minHeap)) {
        left = extractMin(minHeap);
        right = extractMin(minHeap);

        // '$' is a special value for internal nodes, freq is sum of child freqs
        top = newNode('$', left->freq + right->freq);
        top->left = left;
        top->right = right;

        insertMinHeap(minHeap, top);
    }
    struct MinHeapNode* root = extractMin(minHeap);
    free(minHeap->array);
    free(minHeap);
    return root;
}

// Print codes from the root of Huffman Tree
void getCodes(struct MinHeapNode* root, int arr[], int top, char codes[MAX_CHAR][MAX_TREE_HT]) {
    if (root->left) {
        arr[top] = 0;
        getCodes(root->left, arr, top + 1, codes);
    }

    if (root->right) {
        arr[top] = 1;
        getCodes(root->right, arr, top + 1, codes);
    }

    if (isLeaf(root)) {
        int i;
        for (i = 0; i < top; i++) {
            codes[(unsigned char)root->data][i] = arr[i] + '0';
        }
        codes[(unsigned char)root->data][i] = '\0';
    }
}

// Function to free Huffman Tree memory
void freeTree(struct MinHeapNode* root) {
    if (!root) return;
    freeTree(root->left);
    freeTree(root->right);
    free(root);
}

// Function to compress a string and show results
void compressString(char *text) {
    int freq[MAX_CHAR] = {0};
    int len = strlen(text);
    if (len == 0) {
        printf("Empty string cannot be compressed.\n");
        return;
    }

    for (int i = 0; i < len; i++) {
        freq[(unsigned char)text[i]]++;
    }

    char unique_chars[MAX_CHAR];
    int char_freqs[MAX_CHAR];
    int size = 0;

    for (int i = 0; i < MAX_CHAR; i++) {
        if (freq[i] > 0) {
            unique_chars[size] = (char)i;
            char_freqs[size] = freq[i];
            size++;
        }
    }

    // Edge case: string with only one unique character
    struct MinHeapNode* root;
    char codes[MAX_CHAR][MAX_TREE_HT] = {{0}};
    
    if (size == 1) {
        codes[(unsigned char)unique_chars[0]][0] = '0';
        codes[(unsigned char)unique_chars[0]][1] = '\0';
        root = newNode(unique_chars[0], char_freqs[0]);
    } else {
        root = buildHuffmanTree(unique_chars, char_freqs, size);
        int arr[MAX_TREE_HT];
        getCodes(root, arr, 0, codes);
    }

    printf("\n--- Huffman Codes Generated ---\n");
    printf("%-10s | %-10s | %-15s\n", "Character", "Frequency", "Huffman Code");
    printf("---------------------------------------------\n");
    for (int i = 0; i < size; i++) {
        char c = unique_chars[i];
        if (c == '\n') {
            printf("%-10s | %-10d | %-15s\n", "\\n", char_freqs[i], codes[(unsigned char)c]);
        } else if (c == '\t') {
            printf("%-10s | %-10d | %-15s\n", "\\t", char_freqs[i], codes[(unsigned char)c]);
        } else {
            printf("%-10c | %-10d | %-15s\n", c, char_freqs[i], codes[(unsigned char)c]);
        }
    }

    printf("\nOriginal Text: %s\n", text);
    printf("Compressed Bitstream: ");
    int total_bits = 0;
    for (int i = 0; i < len; i++) {
        printf("%s", codes[(unsigned char)text[i]]);
        total_bits += strlen(codes[(unsigned char)text[i]]);
    }
    printf("\n");

    int original_bits = len * 8;
    double compression_ratio = (double)original_bits / total_bits;
    double space_savings = (1.0 - ((double)total_bits / original_bits)) * 100.0;

    printf("\n--- Compression Metrics ---\n");
    printf("Original Size: %d bits (%d bytes)\n", original_bits, len);
    printf("Compressed Size: %d bits (~%d bytes)\n", total_bits, (total_bits + 7) / 8);
    printf("Compression Ratio: %.2f\n", compression_ratio);
    printf("Space Savings: %.2f%%\n", space_savings);

    if (size > 1) {
        freeTree(root);
    } else {
        free(root);
    }
}

// Function to generate random string of given size
void generateRandomText(char *text, int length) {
    char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ";
    int charset_size = sizeof(charset) - 1;
    for (int i = 0; i < length; i++) {
        text[i] = charset[rand() % charset_size];
    }
    text[length] = '\0';
}

void performanceAnalysis() {
    int sizes[] = {100, 1000, 5000, 10000, 20000, 50000};
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    printf("\n--- Performance Analysis (Huffman Coding: O(N + C log C)) ---\n");
    printf("%-20s | %-20s\n", "Text Length (N)", "Time Taken (seconds)");
    printf("---------------------------------------------\n");

    for (int i = 0; i < num_sizes; i++) {
        int n = sizes[i];
        char *text = (char *)malloc((n + 1) * sizeof(char));
        generateRandomText(text, n);

        clock_t start = clock();
        
        // Frequencies computation
        int freq[MAX_CHAR] = {0};
        for (int j = 0; j < n; j++) {
            freq[(unsigned char)text[j]]++;
        }
        
        char unique_chars[MAX_CHAR];
        int char_freqs[MAX_CHAR];
        int size = 0;
        for (int j = 0; j < MAX_CHAR; j++) {
            if (freq[j] > 0) {
                unique_chars[size] = (char)j;
                char_freqs[size] = freq[j];
                size++;
            }
        }
        
        struct MinHeapNode* root = buildHuffmanTree(unique_chars, char_freqs, size);
        int arr[MAX_TREE_HT];
        char codes[MAX_CHAR][MAX_TREE_HT] = {{0}};
        getCodes(root, arr, 0, codes);
        
        // Simulate encoding
        volatile int dummy = 0;
        for (int j = 0; j < n; j++) {
            dummy += codes[(unsigned char)text[j]][0];
        }

        clock_t end = clock();
        double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("%-20d | %-20f\n", n, time_taken);

        freeTree(root);
        free(text);
    }
    printf("---------------------------------------------\n");
}

int main() {
    int choice;
    char text[4096];
    srand(time(0));

    while (1) {
        printf("\n=========================================\n");
        printf(" TELECOM TEXT COMPRESSION SYSTEM (HUFFMAN) \n");
        printf("=========================================\n");
        printf("1. Compress String\n");
        printf("2. Run Performance Analysis\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        
        if (scanf("%d", &choice) != 1) {
            break;
        }
        // Consume newline character
        getchar();

        switch (choice) {
            case 1:
                printf("Enter text to compress: ");
                fgets(text, sizeof(text), stdin);
                // Remove trailing newline
                text[strcspn(text, "\n")] = 0;
                compressString(text);
                break;
            case 2:
                performanceAnalysis();
                break;
            case 3:
                printf("Exiting program...\n");
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }
    return 0;
}
