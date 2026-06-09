import random
import time
import heapq

n = 100

graph = [[] for _ in range(n)]

for u in range(n):

    for _ in range(5):

        v = random.randint(0, n - 1)

        weight = random.randint(1, 20)

        graph[u].append((v, weight))

def dijkstra(source):

    dist = [float('inf')] * n

    dist[source] = 0

    pq = [(0, source)]

    while pq:

        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:

            new_dist = dist[u] + weight

            if new_dist < dist[v]:

                dist[v] = new_dist

                heapq.heappush(
                    pq,
                    (new_dist, v)
                )

    return dist

start = time.time()

distances = dijkstra(0)

end = time.time()

print("Shortest Distances:")

for i in range(10):

    print(
        f"Node {i} : {distances[i]}"
    )

print()

print("Execution Time =",
      end - start,
      "seconds")
