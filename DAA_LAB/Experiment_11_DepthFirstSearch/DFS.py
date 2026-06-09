import random
import time

n = 10

graph = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        graph[i][j] = random.randint(0,1)

visited = [False] * n

discovery = [0] * n
finish = [0] * n

timer = 0

def dfs(node):

    global timer

    visited[node] = True

    timer += 1
    discovery[node] = timer

    for i in range(n):

        if graph[node][i] and not visited[i]:

            dfs(i)

    timer += 1
    finish[node] = timer


start = time.time()

dfs(0)

end = time.time()

print("Node\tDiscovery\tFinish")

for i in range(n):

    print(
        i,
        "\t",
        discovery[i],
        "\t\t",
        finish[i]
    )

print()

print(
    "Execution Time =",
    end-start,
    "seconds"
)
