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
