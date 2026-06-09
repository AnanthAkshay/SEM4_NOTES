import random
import time

n = 1001

waiting_time = [
    random.randint(1, 500)
    for _ in range(n)
]

start = time.time()

waiting_time.sort()

median = waiting_time[len(waiting_time)//2]

end = time.time()

print("Median Waiting Time =",
      median, "minutes")

print("Execution Time =",
      end - start,
      "seconds")
