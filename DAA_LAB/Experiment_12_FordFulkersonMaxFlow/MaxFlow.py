from collections import deque
import time

INF = float('inf')

def bfs(cap, source, sink, parent):

    n = len(cap)

    visited = [False] * n

    queue = deque([source])

    visited[source] = True

    while queue:

        u = queue.popleft()

        for v in range(n):

            if (not visited[v]
                and cap[u][v] > 0):

                visited[v] = True

                parent[v] = u

                if v == sink:
                    return True

                queue.append(v)

    return False


def max_flow(cap, source, sink):

    n = len(cap)

    parent = [-1] * n

    flow = 0

    while bfs(
        cap,
        source,
        sink,
        parent
    ):

        path_flow = INF

        v = sink

        while v != source:

            u = parent[v]

            path_flow = min(
                path_flow,
                cap[u][v]
            )

            v = u

        v = sink

        while v != source:

            u = parent[v]

            cap[u][v] -= path_flow

            cap[v][u] += path_flow

            v = u

        flow += path_flow

    return flow


graph = [
 [0,16,13,0,0,0],
 [0,0,10,12,0,0],
 [0,0,0,0,14,0],
 [0,0,9,0,0,20],
 [0,0,0,7,0,4],
 [0,0,0,0,0,0]
]

start = time.time()

result = max_flow(
    graph,
    0,
    5
)

end = time.time()

print(
    "Maximum Water Flow =",
    result,
    "units"
)

print(
    "Execution Time =",
    end-start,
    "seconds"
)
