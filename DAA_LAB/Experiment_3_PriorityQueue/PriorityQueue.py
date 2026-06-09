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
