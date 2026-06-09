import random
import time

parent = []
rank = []

def make_set(n):

    global parent, rank

    parent = [i for i in range(n)]
    rank = [0] * n

def find(x):

    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):

    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return

    if rank[root_x] < rank[root_y]:

        parent[root_x] = root_y

    elif rank[root_x] > rank[root_y]:

        parent[root_y] = root_x

    else:

        parent[root_y] = root_x
        rank[root_x] += 1


n = 1000

make_set(n)

start = time.time()

for _ in range(500):

    a = random.randint(0, n - 1)
    b = random.randint(0, n - 1)

    union(a, b)

end = time.time()

print("Friend Groups:")

for i in range(10):

    print(
        f"User {i} -> Group {find(i)}"
    )

print()

print("Execution Time =",
      end - start,
      "seconds")
