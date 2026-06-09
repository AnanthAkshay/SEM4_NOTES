import random
import time

def counting_sort(arr):

    count = [0] * 101

    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, 101):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):

        output[count[arr[i]] - 1] = arr[i]

        count[arr[i]] -= 1

    return output


n = 1000

marks = [random.randint(0, 100)
         for _ in range(n)]

start = time.time()

marks = counting_sort(marks)

end = time.time()

print("First 20 Sorted Marks:")
print(marks[:20])

print("Execution Time =",
      end - start,
      "seconds")
